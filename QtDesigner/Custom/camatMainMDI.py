# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camatMainMDI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MDIMainWindow(object):
    def setupUi(self, MDIMainWindow):
        MDIMainWindow.setObjectName("MDIMainWindow")
        MDIMainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MDIMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName("mdiArea")
        self.verticalLayout.addWidget(self.mdiArea)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MDIMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MDIMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MDIMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MDIMainWindow)
        self.statusbar.setObjectName("statusbar")
        MDIMainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(MDIMainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionClose = QtWidgets.QAction(MDIMainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MDIMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MDIMainWindow)

    def retranslateUi(self, MDIMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MDIMainWindow.setWindowTitle(_translate("MDIMainWindow", "MVP1"))
        self.menuFile.setTitle(_translate("MDIMainWindow", "File"))
        self.actionLoad.setText(_translate("MDIMainWindow", "Load"))
        self.actionClose.setText(_translate("MDIMainWindow", "Close"))

