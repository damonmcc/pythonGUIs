# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camatWidgetFolderTree.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetFolderTree(object):
    def setupUi(self, WidgetFolderTree):
        WidgetFolderTree.setObjectName("WidgetFolderTree")
        WidgetFolderTree.resize(486, 418)
        self.verticalLayout = QtWidgets.QVBoxLayout(WidgetFolderTree)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeView = QtWidgets.QTreeView(WidgetFolderTree)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonOpen = QtWidgets.QPushButton(WidgetFolderTree)
        self.pushButtonOpen.setObjectName("pushButtonOpen")
        self.horizontalLayout.addWidget(self.pushButtonOpen)
        self.pushButtonClose = QtWidgets.QPushButton(WidgetFolderTree)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.horizontalLayout.addWidget(self.pushButtonClose)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(WidgetFolderTree)
        QtCore.QMetaObject.connectSlotsByName(WidgetFolderTree)

    def retranslateUi(self, WidgetFolderTree):
        _translate = QtCore.QCoreApplication.translate
        WidgetFolderTree.setWindowTitle(_translate("WidgetFolderTree", "Folder Tree"))
        self.pushButtonOpen.setText(_translate("WidgetFolderTree", "Open"))
        self.pushButtonClose.setText(_translate("WidgetFolderTree", "Close"))

