# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_project.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from project import Ui_ProjectWindow

import MySQLdb as mdb

class Ui_CreateProjectInfoWindow(object):
    def setupUi(self, CreateProjectInfoWindow):
        CreateProjectInfoWindow.setObjectName("CreateProjectInfoWindow")
        CreateProjectInfoWindow.resize(553, 818)
        self.centralwidget = QtWidgets.QWidget(CreateProjectInfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 591, 51))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 80, 1161, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 481, 51))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 481, 51))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 160, 481, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 270, 481, 101))
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 380, 481, 51))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 420, 481, 51))
        self.label_6.setObjectName("label_6")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 480, 481, 211))
        self.textEdit_2.setObjectName("textEdit_2")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(230, 720, 89, 25))
        self.saveBtn.clicked.connect(self.create_project)
        self.saveBtn.clicked.connect(CreateProjectInfoWindow.close)
        
        font = QtGui.QFont()
        font.setPointSize(14)
        self.saveBtn.setFont(font)
        self.saveBtn.setObjectName("saveBtn")
        CreateProjectInfoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CreateProjectInfoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 22))
        self.menubar.setObjectName("menubar")
        self.menuInteractive_System_Modelling = QtWidgets.QMenu(self.menubar)
        self.menuInteractive_System_Modelling.setObjectName("menuInteractive_System_Modelling")
        CreateProjectInfoWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CreateProjectInfoWindow)
        self.statusbar.setObjectName("statusbar")
        CreateProjectInfoWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuInteractive_System_Modelling.menuAction())

        self.retranslateUi(CreateProjectInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateProjectInfoWindow)

    def create_project(self):
        db = mdb.connect('127.0.0.1', 'root', '', 'interSys')
        with db:
            cur = db.cursor()
 
            cur.execute("INSERT INTO projects(name, short_descr, long_descr)"
                        "VALUES('%s', '%s', '%s')" % (''.join(self.lineEdit.text()),
                                                  ''.join(self.textEdit.toPlainText()),
                                                  ''.join(self.textEdit_2.toPlainText())))
            #cur_name = 'Project: ' + self.lineEdit.text()
            #cur_vers = 'Version #1.0: New '
 
            db.commit()
            QtWidgets.QMessageBox.about(self.centralwidget,'Connection', 'Data Inserted Successfully')
        #open the project
        cur_name = 'Project: ' + self.lineEdit.text()
        cur_vers = 'Version #1.0: New '
        self.ProjectWindow = QtWidgets.QMainWindow()
        self.ui = Ui_ProjectWindow()
        self.ui.setupUi(self.ProjectWindow)
        self.ui.label.setText("Project: " + self.lineEdit.text())
        #self.ProjectWindow.label.setText(cur_name)
        #self.ProjectWindow.label_2.setText(cur_vers)
        #self.ProjectWindow.displayInfo()
        self.ProjectWindow.show()
        self.ui.label.setText(cur_name)
        self.ui.label_2.setText(cur_vers)

    def retranslateUi(self, CreateProjectInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateProjectInfoWindow.setWindowTitle(_translate("CreateProjectInfoWindow", "MainWindow"))
        self.label.setText(_translate("CreateProjectInfoWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">Edit Project Information</span></p></body></html>"))
        self.label_2.setText(_translate("CreateProjectInfoWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Project Name</span></p></body></html>"))
        self.label_4.setText(_translate("CreateProjectInfoWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Short Description</span></p></body></html>"))
        self.label_5.setText(_translate("CreateProjectInfoWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Long Description</span></p></body></html>"))
        self.label_6.setText(_translate("CreateProjectInfoWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#888a85;\">Optional</span></p></body></html>"))
        self.saveBtn.setText(_translate("CreateProjectInfoWindow", "Save"))
        self.menuInteractive_System_Modelling.setTitle(_translate("CreateProjectInfoWindow", "1"))

