# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Experiment.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)

import MySQLdb as mdb
from contextlib import closing


from add_to_exp import Ui_AddToExpWindow
from edit_item_repr_in_exp import Ui_EditItemReprInExpWindow


class Ui_ExperimentWindow(object):
    def setupUi(self, ExperimentWindow):
        ExperimentWindow.setObjectName("ExperimentWindow")
        ExperimentWindow.resize(1159, 861)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ExperimentWindow.sizePolicy().hasHeightForWidth())
        ExperimentWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(ExperimentWindow)
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
        self.factsTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.factsTableWidget.setGeometry(QtCore.QRect(80, 180, 991, 251))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.factsTableWidget.setFont(font)
        self.factsTableWidget.setLineWidth(1)
        self.factsTableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.factsTableWidget.setShowGrid(True)
        self.factsTableWidget.setWordWrap(True)
        self.factsTableWidget.setCornerButtonEnabled(True)
        self.factsTableWidget.setObjectName("factsTableWidget")
        self.factsTableWidget.setColumnCount(6)
        self.factsTableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.factsTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.factsTableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.factsTableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.factsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        self.factsTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.factsTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.factsTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.factsTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.factsTableWidget.setHorizontalHeaderItem(5, item)
        self.factsTableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.factsTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.factsTableWidget.horizontalHeader().setDefaultSectionSize(162)
        self.factsTableWidget.horizontalHeader().setMinimumSectionSize(71)
        self.factsTableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.factsTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.factsTableWidget.verticalHeader().setDefaultSectionSize(26)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 351, 51))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 351, 51))
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font)
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(510, 760, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addBtn.setFont(font)
        self.addBtn.setObjectName("addBtn")
        self.editBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editBtn.setGeometry(QtCore.QRect(700, 760, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.editBtn.setFont(font)
        self.editBtn.setObjectName("editBtn")
        self.deleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteBtn.setGeometry(QtCore.QRect(890, 760, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.deleteBtn.setFont(font)
        self.deleteBtn.setObjectName("deleteBtn")
        self.questTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.questTableWidget.setGeometry(QtCore.QRect(80, 490, 991, 251))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.questTableWidget.setFont(font)
        self.questTableWidget.setLineWidth(1)
        self.questTableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.questTableWidget.setShowGrid(True)
        self.questTableWidget.setWordWrap(True)
        self.questTableWidget.setCornerButtonEnabled(True)
        self.questTableWidget.setObjectName("questTableWidget")
        self.questTableWidget.setColumnCount(6)
        self.questTableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.questTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.questTableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.questTableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.questTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        self.questTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.questTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.questTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.questTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.questTableWidget.setHorizontalHeaderItem(5, item)
        self.questTableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.questTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.questTableWidget.horizontalHeader().setDefaultSectionSize(162)
        self.questTableWidget.horizontalHeader().setMinimumSectionSize(71)
        self.questTableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.questTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.questTableWidget.verticalHeader().setDefaultSectionSize(26)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(520, 440, 151, 51))
        self.label_5.setObjectName("label_5")
        self.updateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.updateBtn.setGeometry(QtCore.QRect(700, 10, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.updateBtn.setFont(font)
        self.updateBtn.setObjectName("updateBtn")
        self.factsTableWidget.raise_()
        self.label.raise_()
        self.line.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.addBtn.raise_()
        self.editBtn.raise_()
        self.deleteBtn.raise_()
        self.questTableWidget.raise_()
        self.label_5.raise_()
        ExperimentWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ExperimentWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1159, 22))
        self.menubar.setObjectName("menubar")
        self.menuInteractive_System_Modelling = QtWidgets.QMenu(self.menubar)
        self.menuInteractive_System_Modelling.setObjectName("menuInteractive_System_Modelling")
        ExperimentWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ExperimentWindow)
        self.statusbar.setObjectName("statusbar")
        ExperimentWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuInteractive_System_Modelling.menuAction())

        self.retranslateUi(ExperimentWindow)
        QtCore.QMetaObject.connectSlotsByName(ExperimentWindow)

        self.version_id = QtWidgets.QLabel(self.centralwidget)
        self.version_id.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.version_id.setObjectName("version_id")

        self.updateBtn.clicked.connect(self.getItems)
        self.addBtn.clicked.connect(self.addItem)
        self.editBtn.clicked.connect(self.editItem)
        self.deleteBtn.clicked.connect(self.deleteItem)
        self.factsTableWidget.itemClicked.connect(self.pressedFacts)
        self.questTableWidget.itemClicked.connect(self.pressedQuestions)


    def getItems(self):
        version_id = int(self.version_id.text())
        self.factsTableWidget.setRowCount(0)
        self.questTableWidget.setRowCount(0)
        db = mdb.connect('127.0.0.1', 'root', '', 'interSys')
        with closing(db.cursor()) as cur:
            cur.execute("SELECT * FROM experiment WHERE version_id = '%i' ORDER BY id" % (version_id))
            items = cur.fetchall()

            i = 0
            j = 0
            for item in items:
                if item[3] == "fact":
                    self.factsTableWidget.setRowCount(i+1)
                    self.factsTableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(item[2])))
                    self.factsTableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(item[4])))
                    self.factsTableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(item[5])))
                    self.factsTableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(item[6])))
                    self.factsTableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(item[10])))
                    self.factsTableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(item[11])))
                    i+=1
                elif item[3] == "question":
                    self.questTableWidget.setRowCount(j+1)
                    self.questTableWidget.setItem(j, 0, QtWidgets.QTableWidgetItem(str(item[2])))
                    self.questTableWidget.setItem(j, 1, QtWidgets.QTableWidgetItem(str(item[8])+" "+str(item[7])+" "+str(item[9])+"?"))
                    self.questTableWidget.setItem(j, 2, QtWidgets.QTableWidgetItem(str(item[5])))
                    self.questTableWidget.setItem(j, 3, QtWidgets.QTableWidgetItem(str(item[6])))
                    self.questTableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(item[10])))
                    self.questTableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(item[11])))
                    j+=1

    def addItem(self):
        self.AddToExpWindow = QtWidgets.QMainWindow()
        self.ui = Ui_AddToExpWindow()
        self.ui.setupUi(self.AddToExpWindow)
        self.ui.version_id.setText(self.version_id.text())
        self.AddToExpWindow.show()

    def editItem(self):

        tableItems=self.factsTableWidget.selectedItems()
        if tableItems:
            curr_row = self.factsTableWidget.currentRow()
            fact = True
        else:
            curr_row = self.questTableWidget.currentRow()
            fact = False

        curr_col = 0
        if curr_row == -1 and curr_col == -1:
            return 

        if fact:
            cur_dom = self.factsTableWidget.item(curr_row, curr_col).text()
            cur_value = self.factsTableWidget.item(curr_row, curr_col+1).text()
            cur_in_time = self.factsTableWidget.item(curr_row, curr_col+2).text()
            cur_for_time = self.factsTableWidget.item(curr_row, curr_col+3).text()
            repeat = self.factsTableWidget.item(curr_row, curr_col+4).text()
            repeat_in_time = self.factsTableWidget.item(curr_row, curr_col+5).text()
        else:
            cur_dom = self.questTableWidget.item(curr_row, curr_col).text()
            cur_value = self.questTableWidget.item(curr_row, curr_col+1).text()
            cur_in_time = self.questTableWidget.item(curr_row, curr_col+2).text()
            cur_for_time = self.questTableWidget.item(curr_row, curr_col+3).text()
            repeat = self.factsTableWidget.item(curr_row, curr_col+4).text()
            repeat_in_time = self.factsTableWidget.item(curr_row, curr_col+5).text()
                        

        self.EditItemReprInExpWindow = QtWidgets.QMainWindow()
        self.ui = Ui_EditItemReprInExpWindow()
        self.ui.setupUi(self.EditItemReprInExpWindow)
        self.ui.for_lineEdit.setText(cur_for_time)
        self.ui.in_lineEdit.setText(cur_in_time)
        self.ui.repeat_lineEdit.setText(repeat)
        self.ui.in_time_lineEdit.setText(repeat_in_time)
        self.ui.version_id.setText(self.version_id.text())
        self.ui.label_3.setText(cur_dom + " - " + cur_value + " - " + cur_in_time + " - "  + cur_for_time)
        self.ui.origin_dom = cur_dom
        self.ui.origin_value = cur_value
        if fact:
            self.ui.item = "facts"
            self.ui.CatComboBox.setGeometry(QtCore.QRect(200, 260, 311, 41))
            self.ui.TypesComboBox.setGeometry(QtCore.QRect(200, 310, 311, 41))
            self.ui.label_5.setGeometry(QtCore.QRect(20, 260, 121, 31))
            self.ui.label_6.setGeometry(QtCore.QRect(20, 310, 121, 31))

        else:
            self.ui.item = "questions"
            self.ui.CatComboBox.setGeometry(QtCore.QRect(200, 310, 311, 41))
            self.ui.TypesComboBox.setGeometry(QtCore.QRect(200, 260, 311, 41))
            self.ui.label_5.setGeometry(QtCore.QRect(20, 310, 121, 31))
            self.ui.label_6.setGeometry(QtCore.QRect(20, 260, 121, 31))
        self.EditItemReprInExpWindow.show()

    def deleteItem(self):
        version_id = int(self.version_id.text())

        tableItems=self.factsTableWidget.selectedItems()
        if tableItems:
            curr_row = self.factsTableWidget.currentRow()
            fact = True
        else:
            curr_row = self.questTableWidget.currentRow()
            fact = False

        curr_col = 0
        if curr_row == -1 and curr_col == -1:
            return 
        if fact:
            cur_dom = self.factsTableWidget.item(curr_row, curr_col).text()
            cur_value = self.factsTableWidget.item(curr_row, curr_col+1).text()
        else:
            cur_dom = self.questTableWidget.item(curr_row, curr_col).text()
            cur_value = self.questTableWidget.item(curr_row, curr_col+1).text()

        reply = QMessageBox.question(self.centralwidget, "Delete fact representation", "Are you sure you want to delete this fact representation?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            
            db = mdb.connect('127.0.0.1', 'root', '', 'interSys')
            with closing(db.cursor()) as cur:
                cur.execute("DELETE FROM experiment WHERE version_id = '%i' AND domain = '%s' AND value = '%s'" % (version_id, cur_dom, cur_value))
                db.commit()
                if fact:
                    self.factsTableWidget.removeRow(curr_row)
                else:
                    self.questTableWidget.removeRow(curr_row)
            db.close()
            self.questTableWidget.clearSelection()
            self.factsTableWidget.clearSelection()

        else:
            return

    def pressedFacts(self):
        self.questTableWidget.clearSelection()

    def pressedQuestions(self):
        self.factsTableWidget.clearSelection()


    def retranslateUi(self, ExperimentWindow):
        _translate = QtCore.QCoreApplication.translate
        ExperimentWindow.setWindowTitle(_translate("ExperimentWindow", "MainWindow"))
        self.label.setText(_translate("ExperimentWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">Experiment</span></p></body></html>"))
        self.label_4.setText(_translate("ExperimentWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Facts</span></p></body></html>"))
        item = self.factsTableWidget.verticalHeaderItem(0)
        item.setText(_translate("ExperimentWindow", "1"))
        item = self.factsTableWidget.verticalHeaderItem(1)
        item.setText(_translate("ExperimentWindow", "2"))
        item = self.factsTableWidget.verticalHeaderItem(2)
        item.setText(_translate("ExperimentWindow", "3"))
        item = self.factsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ExperimentWindow", "Domain"))
        item = self.factsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ExperimentWindow", "Fact"))
        item = self.factsTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ExperimentWindow", "Starting In"))
        item = self.factsTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ExperimentWindow", "Available For"))
        item = self.factsTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ExperimentWindow", "Repeat"))
        item = self.factsTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ExperimentWindow", "In time"))
        __sortingEnabled = self.factsTableWidget.isSortingEnabled()
        self.factsTableWidget.setSortingEnabled(False)
        self.factsTableWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("ExperimentWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Project: Animal-Dog</span></p></body></html>"))
        self.label_3.setText(_translate("ExperimentWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Version #1.1: New</span></p></body></html>"))
        self.addBtn.setText(_translate("ExperimentWindow", "Add"))
        self.editBtn.setText(_translate("ExperimentWindow", "Edit"))
        self.deleteBtn.setText(_translate("ExperimentWindow", "Delete"))
        self.updateBtn.setText(_translate("ShortTermMemWindow", "Update"))
        item = self.questTableWidget.verticalHeaderItem(0)
        item.setText(_translate("ExperimentWindow", "1"))
        item = self.questTableWidget.verticalHeaderItem(1)
        item.setText(_translate("ExperimentWindow", "2"))
        item = self.questTableWidget.verticalHeaderItem(2)
        item.setText(_translate("ExperimentWindow", "3"))
        item = self.questTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ExperimentWindow", "Domain"))
        item = self.questTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ExperimentWindow", "Question"))
        item = self.questTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ExperimentWindow", "Starting In"))
        item = self.questTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ExperimentWindow", "Available For"))
        item = self.questTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ExperimentWindow", "Repeat"))
        item = self.questTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ExperimentWindow", "In time"))
        __sortingEnabled = self.questTableWidget.isSortingEnabled()
        self.questTableWidget.setSortingEnabled(False)
        self.questTableWidget.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("ExperimentWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Questions</span></p></body></html>"))
        self.menuInteractive_System_Modelling.setTitle(_translate("ExperimentWindow", "1"))

