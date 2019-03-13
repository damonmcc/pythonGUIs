

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget

from pyqtgraph.widgets.RawImageWidget import RawImageWidget


class VideoWidget(QWidget):
    """Widget defined in Qt Designer"""

    def __init__(self, parent=None):
        # initialization of Qt MainWindow widget
        super(VideoWidget, self).__init__(parent)
        # set the "canvas" to the RawImage widget
        self.rawImg = RawImageWidget(QWidget())
        # create a vertical box layout
        self.vbl = QVBoxLayout()
        # add widget to vertical box
        self.vbl.addWidget(self.rawImg)
        # set the layout to the vertical box
        self.setLayout(self.vbl)
