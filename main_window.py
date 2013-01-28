# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Mon Jan 28 12:05:36 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1161, 551)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.backupInfoText = QtGui.QTextEdit(self.centralwidget)
        self.backupInfoText.setMinimumSize(QtCore.QSize(260, 0))
        self.backupInfoText.setMaximumSize(QtCore.QSize(300, 16777215))
        self.backupInfoText.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.backupInfoText.setObjectName("backupInfoText")
        self.verticalLayout.addWidget(self.backupInfoText)
        self.fileTree = QtGui.QTreeWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fileTree.sizePolicy().hasHeightForWidth())
        self.fileTree.setSizePolicy(sizePolicy)
        self.fileTree.setMinimumSize(QtCore.QSize(260, 0))
        self.fileTree.setMaximumSize(QtCore.QSize(300, 16777215))
        self.fileTree.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.fileTree.setAutoExpandDelay(-1)
        self.fileTree.setObjectName("fileTree")
        self.fileTree.headerItem().setText(0, "Name")
        self.verticalLayout.addWidget(self.fileTree)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy)
        self.mdiArea.setObjectName("mdiArea")
        self.horizontalLayout.addWidget(self.mdiArea)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fileInfoText = QtGui.QTextEdit(self.centralwidget)
        self.fileInfoText.setMaximumSize(QtCore.QSize(250, 16777215))
        self.fileInfoText.setObjectName("fileInfoText")
        self.verticalLayout_2.addWidget(self.fileInfoText)
        self.imagePreviewLabel = QtGui.QLabel(self.centralwidget)
        self.imagePreviewLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.imagePreviewLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.imagePreviewLabel.setText("")
        self.imagePreviewLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imagePreviewLabel.setObjectName("imagePreviewLabel")
        self.verticalLayout_2.addWidget(self.imagePreviewLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1161, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNext = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNext.setIcon(icon)
        self.actionNext.setObjectName("actionNext")
        self.actionPrev = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrev.setIcon(icon1)
        self.actionPrev.setObjectName("actionPrev")
        self.actionTile = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/tile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTile.setIcon(icon2)
        self.actionTile.setObjectName("actionTile")
        self.toolBar.addAction(self.actionPrev)
        self.toolBar.addAction(self.actionTile)
        self.toolBar.addAction(self.actionNext)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "iPBA 2", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTree.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTree.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTree.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNext.setText(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNext.setToolTip(QtGui.QApplication.translate("MainWindow", "Next window", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrev.setText(QtGui.QApplication.translate("MainWindow", "Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrev.setToolTip(QtGui.QApplication.translate("MainWindow", "Previous window", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTile.setText(QtGui.QApplication.translate("MainWindow", "Tile", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTile.setToolTip(QtGui.QApplication.translate("MainWindow", "Tile windows", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
