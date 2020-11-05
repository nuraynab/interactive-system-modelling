# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)

from save_version import Ui_SaveVersionWindow

import MySQLdb as mdb

db = mdb.connect('127.0.0.1', 'root', '', 'interSys')

class Ui_ProjectWindow(QWidget):
    def setupUi(self, ProjectWindow):
        ProjectWindow.setObjectName("ProjectWindow")
        ProjectWindow.resize(1162, 861)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProjectWindow.sizePolicy().hasHeightForWidth())
        ProjectWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(ProjectWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.saveVerBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveVerBtn.setGeometry(QtCore.QRect(790, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.saveVerBtn.setFont(font)
        self.saveVerBtn.setObjectName("saveVerBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 591, 51))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 1161, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 401, 51))
        self.label_2.setObjectName("label_2")
        self.ExpBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ExpBtn.setGeometry(QtCore.QRect(400, 170, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ExpBtn.setFont(font)
        self.ExpBtn.setObjectName("ExpBtn")
        self.openBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openBtn.setGeometry(QtCore.QRect(818, 744, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.openBtn.setFont(font)
        self.openBtn.setObjectName("openBtn")
        self.editDatabaseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editDatabaseBtn.setGeometry(QtCore.QRect(490, 10, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.editDatabaseBtn.setFont(font)
        self.editDatabaseBtn.setObjectName("editDatabaseBtn")
        self.runBtn = QtWidgets.QPushButton(self.centralwidget)
        self.runBtn.setGeometry(QtCore.QRect(690, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.runBtn.setFont(font)
        self.runBtn.setObjectName("runBtn")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(100, 230, 941, 451))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(120, 280, 621, 381))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(140, 330, 311, 311))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.EnvBtn = QtWidgets.QPushButton(self.centralwidget)
        self.EnvBtn.setGeometry(QtCore.QRect(740, 170, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EnvBtn.setFont(font)
        self.EnvBtn.setObjectName("EnvBtn")
        self.SensMBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SensMBtn.setGeometry(QtCore.QRect(770, 290, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SensMBtn.setFont(font)
        self.SensMBtn.setObjectName("SensMBtn")
        self.STMBtn = QtWidgets.QPushButton(self.centralwidget)
        self.STMBtn.setGeometry(QtCore.QRect(770, 500, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.STMBtn.setFont(font)
        self.STMBtn.setObjectName("STMBtn")
        self.ProcMBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ProcMBtn.setGeometry(QtCore.QRect(480, 340, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ProcMBtn.setFont(font)
        self.ProcMBtn.setObjectName("ProcMBtn")
        self.EpisMBtn = QtWidgets.QPushButton(self.centralwidget)
        self.EpisMBtn.setGeometry(QtCore.QRect(170, 420, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EpisMBtn.setFont(font)
        self.EpisMBtn.setObjectName("EpisMBtn")
        self.SemMBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SemMBtn.setGeometry(QtCore.QRect(170, 510, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SemMBtn.setFont(font)
        self.SemMBtn.setObjectName("SemMBtn")
        self.exitVerBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitVerBtn.setGeometry(QtCore.QRect(950, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.exitVerBtn.setFont(font)
        self.exitVerBtn.setObjectName("exitVerBtn")
        ProjectWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ProjectWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1162, 22))
        self.menubar.setObjectName("menubar")
        self.menuInteractive_System_Modelling = QtWidgets.QMenu(self.menubar)
        self.menuInteractive_System_Modelling.setObjectName("menuInteractive_System_Modelling")
        ProjectWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ProjectWindow)
        self.statusbar.setObjectName("statusbar")
        ProjectWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuInteractive_System_Modelling.menuAction())

        self.retranslateUi(ProjectWindow)
        QtCore.QMetaObject.connectSlotsByName(ProjectWindow)

        self.version_name = QtWidgets.QLabel(self.centralwidget)
        self.version_name.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.version_name.setObjectName("version_name")
        self.project_name = QtWidgets.QLabel(self.centralwidget)
        self.project_name.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.project_name.setObjectName("project_name")
        self.version_number = QtWidgets.QLabel(self.centralwidget)
        self.version_number.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.version_number.setObjectName("version_number")
        self.vers_short_descr = QtWidgets.QLabel(self.centralwidget)
        self.vers_short_descr.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.vers_short_descr.setObjectName("vers_short_descr")
        self.vers_long_descr = QtWidgets.QLabel(self.centralwidget)
        self.vers_long_descr.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.vers_long_descr.setObjectName("vers_long_descr")

        self.exitVerBtn.clicked.connect(self.exit_version)
        self.saveVerBtn.clicked.connect(self.save_version)

    def exit_version(self):  
        reply = QMessageBox.question(self, "Exit version", "Do you want to save the changes?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            self.save_version()
        if reply == QMessageBox.No:
            return
        else:
            return

    def save_version(self):  
        self.SaveVersionWindow = QtWidgets.QMainWindow()
        self.ui = Ui_SaveVersionWindow()
        self.ui.setupUi(self.SaveVersionWindow)
        self.ui.version_name.setText(self.version_name.text())
        self.ui.project_name.setText(self.project_name.text())
        self.ui.version_number.setText(self.version_number.text())
        self.ui.vers_short_descr.setText(self.vers_short_descr.text())
        self.ui.vers_long_descr.setText(self.vers_long_descr.text())        
        self.SaveVersionWindow.show()

    def retranslateUi(self, ProjectWindow):
        _translate = QtCore.QCoreApplication.translate
        ProjectWindow.setWindowTitle(_translate("ProjectWindow", "MainWindow"))
        self.saveVerBtn.setText(_translate("ProjectWindow", "Save Version"))
        self.label.setText(_translate("ProjectWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">Project: Animal-Dog</span></p></body></html>"))
        self.label_2.setText(_translate("ProjectWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Version #1.1: Version Name 2</span></p></body></html>"))
        self.ExpBtn.setText(_translate("ProjectWindow", "Experiments"))
        self.openBtn.setText(_translate("ProjectWindow", "Open Component"))
        self.editDatabaseBtn.setText(_translate("ProjectWindow", "Edit Database"))
        self.runBtn.setText(_translate("ProjectWindow", "Run"))
        self.textBrowser.setHtml(_translate("ProjectWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Human Memory</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("ProjectWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Long-Term Memory</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("ProjectWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Declarative Memory</span></p></body></html>"))
        self.EnvBtn.setText(_translate("ProjectWindow", "Environment"))
        self.SensMBtn.setText(_translate("ProjectWindow", "Sensory Memory"))
        self.STMBtn.setText(_translate("ProjectWindow", "Short-Term Memory"))
        self.ProcMBtn.setText(_translate("ProjectWindow", "Procedural Memory"))
        self.EpisMBtn.setText(_translate("ProjectWindow", "Episodic Memory"))
        self.SemMBtn.setText(_translate("ProjectWindow", "Semantic Memory"))
        self.exitVerBtn.setText(_translate("ProjectWindow", "Exit Version"))
        self.menuInteractive_System_Modelling.setTitle(_translate("ProjectWindow", "1"))

