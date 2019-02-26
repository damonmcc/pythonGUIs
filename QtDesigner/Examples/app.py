#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.codementor.io/deepaksingh04/design-simple-dialog-using-pyqt5-designer-tool-ajskrd09n
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from CustomButtonBox import Ui_Dialog
# TODO: 'ModuleNotFoundError: No module named 'PyQt5.sip''


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
