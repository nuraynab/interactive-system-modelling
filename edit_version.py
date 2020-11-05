# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_version.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import MySQLdb as mdb

class Ui_EditVersionInfoWindow(object):
    def setupUi(self, EditVersionInfoWindow):
        EditVersionInfoWindow.setObjectName("EditVersionInfoWindow")
        EditVersionInfoWindow.resize(553, 895)
        self.centralwidget = QtWidgets.QWidget(EditVersionInfoWindow)
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
        self.label_2.setGeometry(QtCore.QRect(30, 190, 481, 51))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 300, 481, 51))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 250, 481, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 360, 481, 101))
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 470, 481, 51))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 510, 481, 51))
        self.label_6.setObjectName("label_6")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 570, 481, 211))
        self.textEdit_2.setObjectName("textEdit_2")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(230, 810, 89, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.saveBtn.setFont(font)
        self.saveBtn.setObjectName("saveBtn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 90, 481, 51))
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(170, 130, 481, 51))
        self.label_7.setObjectName("label_7")
        EditVersionInfoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EditVersionInfoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 22))
        self.menubar.setObjectName("menubar")
        self.menuInteractive_System_Modelling = QtWidgets.QMenu(self.menubar)
        self.menuInteractive_System_Modelling.setObjectName("menuInteractive_System_Modelling")
        EditVersionInfoWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EditVersionInfoWindow)
        self.statusbar.setObjectName("statusbar")
        EditVersionInfoWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuInteractive_System_Modelling.menuAction())

        self.retranslateUi(EditVersionInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(EditVersionInfoWindow)

        self.saveBtn.clicked.connect(self.edit_version)
        self.saveBtn.clicked.connect(EditVersionInfoWindow.close)

    def edit_version(self):
        db = mdb.connect('127.0.0.1', 'root', '', 'interSys')
        with db:
            cur = db.cursor()
            
            cur.execute("UPDATE versions SET name = '%s', short_descr = '%s', long_descr = '%s' WHERE name = '%s'"
                                                 % (''.join(self.lineEdit.text()),
                                                  ''.join(self.textEdit.toPlainText()),
                                                  ''.join(self.textEdit_2.toPlainText()),
                                                  ''.join(self.origin_name)))
            #cur_name = 'Project: ' + self.lineEdit.text()
            #cur_vers = 'Version #1.0: New '
 
            db.commit()
            QtWidgets.QMessageBox.about(self.centralwidget,'Connection', 'Data Edited Successfully')
        

    def retranslateUi(self, EditVersionInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        EditVersionInfoWindow.setWindowTitle(_translate("EditVersionInfoWindow", "MainWindow"))
        self.label.setText(_translate("EditVersionInfoWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">Edit Version Information</span></p></body></html>"))
        self.label_2.setText(_translate("EditVersionInfoWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Version Name</span></p></body></html>"))
        self.label_4.setText(_translate("EditVersionInfoWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Short Description</span></p></body></html>"))
        self.label_5.setText(_translate("EditVersionInfoWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Long Description</span></p></body></html>"))
        self.label_6.setText(_translate("EditVersionInfoWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#888a85;\">Optional</span></p></body></html>"))
        self.saveBtn.setText(_translate("EditVersionInfoWindow", "Save"))
        self.label_3.setText(_translate("EditVersionInfoWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Animal-Dog</span></p></body></html>"))
        self.label_7.setText(_translate("EditVersionInfoWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-style:italic;\">Version #1.1</span></p></body></html>"))
        self.menuInteractive_System_Modelling.setTitle(_translate("EditVersionInfoWindow", "1"))
