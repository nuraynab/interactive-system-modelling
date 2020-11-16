# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_to_database.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import database


class Ui_AddToDatabaseWindow(object):
    def setupUi(self, AddToDatabaseWindow):
        AddToDatabaseWindow.setObjectName("AddToDatabaseWindow")
        AddToDatabaseWindow.resize(513, 419)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddToDatabaseWindow.sizePolicy().hasHeightForWidth())
        AddToDatabaseWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(AddToDatabaseWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 591, 51))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 1161, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(120, 300, 241, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.saveBtn.setFont(font)
        self.saveBtn.setObjectName("saveBtn")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 120, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 190, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        AddToDatabaseWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddToDatabaseWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 513, 22))
        self.menubar.setObjectName("menubar")
        self.menuInteractive_System_Modelling = QtWidgets.QMenu(self.menubar)
        self.menuInteractive_System_Modelling.setObjectName("menuInteractive_System_Modelling")
        AddToDatabaseWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddToDatabaseWindow)
        self.statusbar.setObjectName("statusbar")
        AddToDatabaseWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuInteractive_System_Modelling.menuAction())

        self.retranslateUi(AddToDatabaseWindow)
        QtCore.QMetaObject.connectSlotsByName(AddToDatabaseWindow)

        self.saveBtn.clicked.connect(self.saveItem)
        self.saveBtn.clicked.connect(AddToDatabaseWindow.close)

    def saveItem(self):
        self.DatabaseWindow = QtWidgets.QMainWindow()
        self.ui = database.Ui_DatabaseWindow()
        self.ui.setupUi(self.DatabaseWindow)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        item.setText(self.lineEdit.text())

        if (str(self.comboBox.currentText()) == "Category"):
            self.ui.CatListWidget.addItem(item)
        elif (str(self.comboBox.currentText()) == "Type"):
            self.ui.TypesListWidget.addItem(item)
        elif (str(self.comboBox.currentText()) == "Attribute"):
            self.ui.AttrListWidget.addItem(item)
        elif (str(self.comboBox.currentText()) == "Fact"):
            self.ui.FactsListWidget.addItem(item)
        elif (str(self.comboBox.currentText()) == "Perception"):
            self.ui.PercListWidget.addItem(item)
        elif (str(self.comboBox.currentText()) == "Action"):
            self.ui.ActListWidget.addItem(item)

        self.DatabaseWindow.show()



    def retranslateUi(self, AddToDatabaseWindow):
        _translate = QtCore.QCoreApplication.translate
        AddToDatabaseWindow.setWindowTitle(_translate("AddToDatabaseWindow", "MainWindow"))
        self.label.setText(_translate("AddToDatabaseWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">Add to Database</span></p></body></html>"))
        self.saveBtn.setText(_translate("AddToDatabaseWindow", "Save"))
        self.comboBox.setItemText(0, _translate("AddToDatabaseWindow", "Category"))
        self.comboBox.setItemText(1, _translate("AddToDatabaseWindow", "Type"))
        self.comboBox.setItemText(2, _translate("AddToDatabaseWindow", "Attribute"))
        self.comboBox.setItemText(3, _translate("AddToDatabaseWindow", "Fact"))
        self.comboBox.setItemText(4, _translate("AddToDatabaseWindow", "Perception"))
        self.comboBox.setItemText(5, _translate("AddToDatabaseWindow", "Action"))
        self.menuInteractive_System_Modelling.setTitle(_translate("AddToDatabaseWindow", "1"))


