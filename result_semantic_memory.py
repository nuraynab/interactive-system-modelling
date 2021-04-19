# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ResultsSemanticMemory.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)

import MySQLdb as mdb
from contextlib import closing


from add_to_env import Ui_AddToEnvWindow
from edit_item_repr_in_env import Ui_EditItemReprInEnvWindow


class Ui_ResultsSemanticMemoryWindow(object):
    def setupUi(self, ResultsSemanticMemoryWindow):
        ResultsSemanticMemoryWindow.setObjectName("ResultsSemanticMemoryWindow")
        ResultsSemanticMemoryWindow.resize(1159, 861)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ResultsSemanticMemoryWindow.sizePolicy().hasHeightForWidth())
        ResultsSemanticMemoryWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(ResultsSemanticMemoryWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 591, 51))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 1161, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(550, 130, 151, 51))
        self.label_4.setObjectName("label_4")
        self.oldTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.oldTableWidget.setGeometry(QtCore.QRect(80, 180, 991, 251))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.oldTableWidget.setFont(font)
        self.oldTableWidget.setLineWidth(1)
        self.oldTableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.oldTableWidget.setShowGrid(True)
        self.oldTableWidget.setWordWrap(True)
        self.oldTableWidget.setCornerButtonEnabled(True)
        self.oldTableWidget.setObjectName("oldTableWidget")
        self.oldTableWidget.setColumnCount(3)
        self.oldTableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.oldTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.oldTableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.oldTableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.oldTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        self.oldTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.oldTableWidget.setHorizontalHeaderItem(2, item)
        self.oldTableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.oldTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.oldTableWidget.horizontalHeader().setDefaultSectionSize(324)
        self.oldTableWidget.horizontalHeader().setMinimumSectionSize(71)
        self.oldTableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.oldTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.oldTableWidget.verticalHeader().setDefaultSectionSize(26)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 351, 51))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 351, 51))
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font)
        self.newTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.newTableWidget.setGeometry(QtCore.QRect(80, 490, 991, 251))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.newTableWidget.setFont(font)
        self.newTableWidget.setLineWidth(1)
        self.newTableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.newTableWidget.setShowGrid(True)
        self.newTableWidget.setWordWrap(True)
        self.newTableWidget.setCornerButtonEnabled(True)
        self.newTableWidget.setObjectName("newTableWidget")
        self.newTableWidget.setColumnCount(3)
        self.newTableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.newTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.newTableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.newTableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.newTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        self.newTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.newTableWidget.setHorizontalHeaderItem(2, item)
        self.newTableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.newTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.newTableWidget.horizontalHeader().setDefaultSectionSize(324)
        self.newTableWidget.horizontalHeader().setMinimumSectionSize(71)
        self.newTableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.newTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.newTableWidget.verticalHeader().setDefaultSectionSize(26)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(520, 440, 151, 51))
        self.label_5.setObjectName("label_5")
        self.updateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.updateBtn.setGeometry(QtCore.QRect(500, 10, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.updateBtn.setFont(font)
        self.updateBtn.setObjectName("updateBtn")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(750, 10, 200, 41))
        self.saveBtn.setFont(font)
        self.saveBtn.setObjectName("saveBtn")
        self.oldTableWidget.raise_()
        self.label.raise_()
        self.line.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.newTableWidget.raise_()
        self.label_5.raise_()
        ResultsSemanticMemoryWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ResultsSemanticMemoryWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1159, 22))
        self.menubar.setObjectName("menubar")
        self.menuInteractive_System_Modelling = QtWidgets.QMenu(self.menubar)
        self.menuInteractive_System_Modelling.setObjectName("menuInteractive_System_Modelling")
        ResultsSemanticMemoryWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ResultsSemanticMemoryWindow)
        self.statusbar.setObjectName("statusbar")
        ResultsSemanticMemoryWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuInteractive_System_Modelling.menuAction())

        self.retranslateUi(ResultsSemanticMemoryWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultsSemanticMemoryWindow)

        self.version_id = QtWidgets.QLabel(self.centralwidget)
        self.version_id.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.version_id.setObjectName("version_id")
        self.version_name = QtWidgets.QLabel(self.centralwidget)
        self.version_name.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.version_name.setObjectName("version_name")
        self.project_name = QtWidgets.QLabel(self.centralwidget)
        self.project_name.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.project_name.setObjectName("project_name")
        self.version_number = QtWidgets.QLabel(self.centralwidget)
        self.version_number.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.version_number.setObjectName("version_number")

        self.updateBtn.clicked.connect(self.getItems)
        
    def getItems(self):
        version_id = int(self.version_id.text())
        self.oldTableWidget.setRowCount(0)
        db = mdb.connect('127.0.0.1', 'root', '', 'interSys')
        with closing(db.cursor()) as cur:
            cur.execute("SELECT * FROM sem_mem WHERE version_id = '%i' ORDER BY id" % (version_id))
            fact_repr = cur.fetchall()

            i = 0
            for y in fact_repr:
                self.oldTableWidget.setRowCount(i+1)
                self.oldTableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(y[2])))
                self.oldTableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(y[3])))
                self.oldTableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(y[4])))
                i+=1
        db.close()


    def retranslateUi(self, ResultsSemanticMemoryWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultsSemanticMemoryWindow.setWindowTitle(_translate("ResultsSemanticMemoryWindow", "MainWindow"))
        self.label.setText(_translate("ResultsSemanticMemoryWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">Semantic Memory</span></p></body></html>"))
        self.label_4.setText(_translate("ResultsSemanticMemoryWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Original</span></p></body></html>"))
        item = self.oldTableWidget.verticalHeaderItem(0)
        item.setText(_translate("ResultsSemanticMemoryWindow", "1"))
        item = self.oldTableWidget.verticalHeaderItem(1)
        item.setText(_translate("ResultsSemanticMemoryWindow", "2"))
        item = self.oldTableWidget.verticalHeaderItem(2)
        item.setText(_translate("ResultsSemanticMemoryWindow", "3"))
        item = self.oldTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ResultsSemanticMemoryWindow", "Domain"))
        item = self.oldTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ResultsSemanticMemoryWindow", "Fact"))
        item = self.oldTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ResultsSemanticMemoryWindow", "Retrieval Time (sec)"))
        __sortingEnabled = self.oldTableWidget.isSortingEnabled()
        self.oldTableWidget.setSortingEnabled(False)
        self.oldTableWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("ResultsSemanticMemoryWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Project: Animal-Dog</span></p></body></html>"))
        self.label_3.setText(_translate("ResultsSemanticMemoryWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Version #1.1: New</span></p></body></html>"))
        self.updateBtn.setText(_translate("ShortTermMemWindow", "Update"))
        item = self.newTableWidget.verticalHeaderItem(0)
        item.setText(_translate("ResultsSemanticMemoryWindow", "1"))
        item = self.newTableWidget.verticalHeaderItem(1)
        item.setText(_translate("ResultsSemanticMemoryWindow", "2"))
        item = self.newTableWidget.verticalHeaderItem(2)
        item.setText(_translate("ResultsSemanticMemoryWindow", "3"))
        item = self.newTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ResultsSemanticMemoryWindow", "Domain"))
        item = self.newTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ResultsSemanticMemoryWindow", "fact"))
        item = self.newTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ResultsSemanticMemoryWindow", "Retrieval Time (sec)"))
        __sortingEnabled = self.newTableWidget.isSortingEnabled()
        self.newTableWidget.setSortingEnabled(False)
        self.newTableWidget.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("ResultsSemanticMemoryWindow", "<html><head/><body><p><span style=\" font-size:20pt; width:1000px;\">Current</span></p></body></html>"))
        self.saveBtn.setText(_translate("ResultsSemanticMemoryWindow", "Save"))
        self.menuInteractive_System_Modelling.setTitle(_translate("ResultsSemanticMemoryWindow", "1"))

