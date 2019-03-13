

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget

from pyqtgraph.widgets.GraphicsLayoutWidget import GraphicsLayoutWidget
from pyqtgraph import ImageItem


class PyqtgraphGraphicsWidget(QWidget):
    """Widget defined in Qt Designer"""

    def __init__(self, parent=None):
        # initialization of Qt MainWindow widget
        super(PyqtgraphGraphicsWidget, self).__init__(parent)
        # # set the "canvas" to the RawImage widget
        # self.rawImg = RawImageWidget(QWidget())
        # # create a vertical box layout
        # self.vbl = QVBoxLayout()
        # # add widget to vertical box
        # self.vbl.addWidget(self.rawImg)
        # # set the layout to the vertical box
        # self.setLayout(self.vbl)

        # Create a central Graphics Layout Widget
        self.widget = GraphicsLayoutWidget()
        # self.setCentralWidget(self.win)

        # A plot area (ViewBox + axes) for displaying the image
        self.p1 = self.widget.addPlot()
        # Item for displaying image data
        self.img = ImageItem()
        self.p1.addItem(self.img)

        # create a vertical box layout
        self.vbl = QVBoxLayout()
        # add widget to vertical box
        self.vbl.addWidget(self.widget)
        # set the layout to the vertical box
        self.setLayout(self.vbl)
