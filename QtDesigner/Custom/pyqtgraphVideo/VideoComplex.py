# -*- coding: utf-8 -*-
"""
Loads a tiff into an embedded pyqtgraph widget made in Qt Designer
and converted with pyuic5. Includes histogram widget and isocurve control
"""

import sys
from imageio import volread
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from pyqtgraph.Qt import QtCore
import numpy as np
import pyqtgraph as pg
import pyqtgraph.ptime as ptime

from QtDesigner.Custom.pyqtgraphVideo.MainWindowComplex import Ui_MainWindow


class VideoMainWindow(QMainWindow, Ui_MainWindow):
    """Customization for Qt Designer created window"""

    def __init__(self, parent=None):
        # initialization of the superclass
        super(VideoMainWindow, self).__init__(parent)
        # setup the GUI
        self.setupUi(self)
        pg.setConfigOptions(background=pg.mkColor(0.5))
        pg.setConfigOptions(foreground=pg.mkColor(0.3))
        self.setWindowTitle('pyqtgraph example: Image Analysis')

        # Preserve plot area's aspect ration so image always scales correctly
        self.graphicsView.p1.setAspectLocked(True)

        # Use a file dialog to choose tiff stack
        file, mask = QFileDialog.getOpenFileName(self, 'Open a .tif/.tiff stack')
        # Read image data
        self.img_data_raw = volread(file)
        frames = self.img_data_raw.shape[0]

        # Transpose second and third axes (y, x) to correct orientation (x, y)
        self.img_data = np.transpose(self.img_data_raw, (0, 2, 1))
        # Flip each frame in the left/right direction, expected to be up/down
        for i in range(frames):
            self.img_data[i] = np.fliplr(self.img_data[i])

        self.ptr = 0
        self.lastTime = ptime.time()
        self.fps = None
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(50)    # 50 ms =~ 20 fps

        # Levels/color control with a histogram
        # TODO try with a HistogramLUTWidget
        self.hist = pg.HistogramLUTItem()
        self.hist.setImageItem(self.graphicsView.img)
        self.graphicsView.widget.addItem(self.hist)

        # Isocurve drawing
        self.iso = pg.IsocurveItem(level=0.8, pen='g')
        self.iso.setParentItem(self.graphicsView.img)
        self.iso.setZValue(5)

        # Draggable line for setting isocurve level
        self.isoLine = pg.InfiniteLine(angle=0, movable=True, pen='g')
        self.hist.vb.addItem(self.isoLine)
        self.hist.vb.setMouseEnabled(y=False)  # makes user interaction a little easier
        self.isoLine.setValue(0.8)
        self.isoLine.setZValue(1000)  # bring iso line above contrast controls
        self.isoLine.sigDragged.connect(self.updateIsocurve)

        # Generate image data
        self.graphicsView.img.setImage(self.img_data[0])
        # self.graphicsView.img.scale(self.img_data.shape[1], self.img_data.shape[2])
        self.hist.setLevels(self.img_data.min(), self.img_data.max())

        # build isocurves from smoothed data
        self.isoLine.setValue(self.img_data.max() / 2)
        self.iso.setData(pg.gaussianFilter(self.img_data[0], (2, 2)))

        # zoom to fit image
        # self.p1.autoRange()
        # self.graphicsView.widget.setAspectLocked(True)

    def updateIsocurve(self):
        self.iso.setLevel(self.isoLine.value())

    # def start(self):
    #     # Display first frame of image stack
    #     # Transpose with .T to correct rotation (caused by axisOrder?)
    #     self.graphicsView.rawImg.setImage(self.img_data[0].T)
    #
    def update(self):
        # Update ImageItem with next frame in stack
        self.graphicsView.img.setImage(self.img_data[self.ptr % self.img_data.shape[0]])
        # Notify histogram item of image change
        self.hist.regionChanged()

        self.ptr += 1
        now = ptime.time()
        dt = now - self.lastTime
        self.lastTime = now
        if self.fps is None:
            self.fps = 1.0 / dt
        else:
            s = np.clip(dt * 3., 0, 1)
            self.fps = self.fps * (1 - s) + (1.0 / dt) * s
        # Show current FPS in status bar
        self.statusBar().showMessage('%0.2f FPS' % self.fps)
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
