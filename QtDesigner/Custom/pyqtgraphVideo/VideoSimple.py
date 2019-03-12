# -*- coding: utf-8 -*-
"""
Loads a tiff into an embedded pyqtgraph widget made in Qt Designer
and converted with pyuic5. Plays the video on loop as quickly as possible.
"""

import sys
from imageio import volread
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QFileSystemModel
from pyqtgraph.Qt import QtGui, QtCore, USE_PYSIDE, USE_PYQT5
import numpy as np
import pyqtgraph as pg
import pyqtgraph.ptime as ptime

from QtDesigner.Custom.pyqtgraphVideo.MainWindow import Ui_MainWindow


class VideoMainWindow(QMainWindow, Ui_MainWindow):
    """Customization for Qt Designer created window"""

    def __init__(self, parent=None):
        # initialization of the superclass
        super(VideoMainWindow, self).__init__(parent)
        # setup the GUI
        self.setupUi(self)
        # Use a file dialog to choose tiff stack
        file, mask = QFileDialog.getOpenFileName(self, 'Open a .tif/.tiff stack')
        # Read image data
        self.img = volread(file)
        # Transpose second and third axes (y, x) to correct orientation (x, y)
        self.img = np.transpose(self.img, (0, 2, 1))
        # for i in range(0, len(self.img)):
        #     self.img[i] = self.img[i].T

        # connect the signals with the slots
        # self.actionLoad.triggered.connect(self.open_tiff)
        # self.actionClose.triggered.connect(self.close)
        # self.actionTIFF.triggered.connect(self.open_tiff)
        # self.actionFolder.triggered.connect(self.open_folder)
        # self.actionStart_ImageProcess.triggered.connect(self.image_process)

        self.ptr = 0
        self.lastTime = ptime.time()
        self.fps = None

        # self.start()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(0)

    def start(self):
        # Display first frame of image stack
        # Transpose with .T to correct rotation (caused by axisOrder?)
        self.graphicsView.rawImg.setImage(self.img[0].T)

    def update(self):
        # Update ImageItem with next frame in stack
        self.graphicsView.rawImg.setImage(self.img[self.ptr % self.img.shape[0]])

        self.ptr += 1
        now = ptime.time()
        dt = now - self.lastTime
        self.lastTime = now
        if self.fps is None:
            self.fps = 1.0 / dt
        else:
            s = np.clip(dt * 3., 0, 1)
            self.fps = self.fps * (1 - s) + (1.0 / dt) * s
        app.processEvents()  # force complete redraw for every plot


# create the GUI application
app = QApplication(sys.argv)
# instantiate the main window
dmw = VideoMainWindow()
# show it
dmw.show()
# start the Qt main loop execution, exiting from this script
# with the same return code as the Qt application
sys.exit(app.exec_())
