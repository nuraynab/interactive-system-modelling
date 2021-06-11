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
from create_version import Ui_CreateVersionInfoWindow
from database import Ui_DatabaseWindow
from sem_mem import Ui_SemMemWindow
from short_term_mem import Ui_ShortTermMemWindow
from environment import Ui_EnvironmentWindow
from experiment import Ui_ExperimentWindow
from results import Ui_ResultsWindow
from question_answer import Ui_QAResWindow
from run_project import Ui_RunProjectWindow
from run_learn import Ui_RunLearnWindow
from result_semantic_memory import Ui_ResultsSemanticMemoryWindow


import MySQLdb as mdb
from contextlib import closing

import subprocess
import re

db = mdb.connect('127.0.0.1', 'root', '', 'interSys')

sem_mem_dict = {}
env_dict = {}
exp_dict = {}

class Ui_ProjectWindow(QWidget):
    def setupUi(self, ProjectWindow):
        ProjectWindow.setObjectName("ProjectWindow")
        ProjectWindow.setFixedSize(1162, 861)
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
        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(40, 10, 591, 51))
        self.label_0.setObjectName("label_0")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 80, 351, 51))
        self.label.setObjectName("label")
        self.label.setFont(font)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 1161, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 351, 51))
        self.label_2.setFont(font)
        self.ExpBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ExpBtn.setGeometry(QtCore.QRect(400, 170, 241, 31))
        self.ExpBtn.setFont(font)
        self.ExpBtn.setObjectName("ExpBtn")
        self.learnBtn = QtWidgets.QPushButton(self.centralwidget)
        self.learnBtn.setGeometry(QtCore.QRect(150, 744, 300, 41))
        self.learnBtn.setFont(font)
        self.learnBtn.setObjectName("learnBtn")
        self.editDatabaseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editDatabaseBtn.setGeometry(QtCore.QRect(520, 10, 191, 41))
        self.editDatabaseBtn.setFont(font)
        self.editDatabaseBtn.setObjectName("editDatabaseBtn")
        self.runBtn = QtWidgets.QPushButton(self.centralwidget)
        self.runBtn.setGeometry(QtCore.QRect(650, 744, 200, 41))
        self.runBtn.setFont(font)
        self.runBtn.setObjectName("runBtn")
        self.resultsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resultsBtn.setGeometry(QtCore.QRect(920, 744, 100, 41))
        self.resultsBtn.setFont(font)
        self.resultsBtn.setObjectName("resultsBtn")
        self.resultsBtn.setEnabled(False)
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
        self.EnvBtn.setFont(font)
        self.EnvBtn.setObjectName("EnvBtn")
        self.SensMBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SensMBtn.setGeometry(QtCore.QRect(770, 290, 241, 31))
        self.SensMBtn.setFont(font)
        self.SensMBtn.setObjectName("SensMBtn")
        self.STMBtn = QtWidgets.QPushButton(self.centralwidget)
        self.STMBtn.setGeometry(QtCore.QRect(770, 500, 241, 31))
        self.STMBtn.setFont(font)
        self.STMBtn.setObjectName("STMBtn")
        self.ProcMBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ProcMBtn.setGeometry(QtCore.QRect(480, 340, 241, 31))
        self.ProcMBtn.setFont(font)
        self.ProcMBtn.setObjectName("ProcMBtn")
        self.EpisMBtn = QtWidgets.QPushButton(self.centralwidget)
        self.EpisMBtn.setGeometry(QtCore.QRect(170, 420, 241, 31))
        self.EpisMBtn.setFont(font)
        self.EpisMBtn.setObjectName("EpisMBtn")
        self.SemMBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SemMBtn.setGeometry(QtCore.QRect(170, 510, 241, 31))
        self.SemMBtn.setFont(font)
        self.SemMBtn.setObjectName("SemMBtn")
        self.exitVerBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitVerBtn.setGeometry(QtCore.QRect(950, 10, 151, 41))
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
        self.vers_short_descr = QtWidgets.QLabel(self.centralwidget)
        self.vers_short_descr.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.vers_short_descr.setObjectName("vers_short_descr")
        self.vers_long_descr = QtWidgets.QLabel(self.centralwidget)
        self.vers_long_descr.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.vers_long_descr.setObjectName("vers_long_descr")

        self.exitVerBtn.clicked.connect(self.exit_version)
        self.saveVerBtn.clicked.connect(self.save_version)

        self.editDatabaseBtn.clicked.connect(self.edit_database)
        self.SemMBtn.clicked.connect(self.sem_mem)
        self.STMBtn.clicked.connect(self.short_term_mem)
        self.EnvBtn.clicked.connect(self.env)
        self.runBtn.clicked.connect(self.run_project)
        self.ExpBtn.clicked.connect(self.exp)
        self.resultsBtn.clicked.connect(self.show_res)
        self.learnBtn.clicked.connect(self.learn)

    def learn(self):
        self.RunLearnWindow = QtWidgets.QMainWindow()
        self.ui = Ui_RunLearnWindow()
        self.ui.setupUi(self.RunLearnWindow)
        self.ui.project_name.setText(self.label.text())
        self.ui.version_name.setText(self.label_2.text())
        self.ui.version_id.setText(self.version_id.text())
        self.RunLearnWindow.show()

    def run_project(self):
        self.resultsBtn.setDisabled(False)
        self.RunProjectWindow = QtWidgets.QMainWindow()
        self.ui = Ui_RunProjectWindow()
        self.ui.setupUi(self.RunProjectWindow)
        self.ui.project_name.setText(self.label.text())
        self.ui.version_name.setText(self.label_2.text())
        self.ui.version_id.setText(self.version_id.text())
        self.RunProjectWindow.show()

    def get_questions(self):
        version_id = int(self.version_id.text())
        db = mdb.connect('127.0.0.1', 'root', '', 'interSys')
        with closing(db.cursor()) as cur:
            cur.execute("""SELECT version_id, domain, item, value, categories, types, attributes FROM experiment WHERE version_id = '%i' AND item = 'question' 
                UNION SELECT version_id, domain, item, value, categories, types, attributes FROM environment WHERE version_id = '%i' AND item = 'question' """ % (version_id, version_id))
            questions = cur.fetchall()
        return questions

    def get_res_stm(self):
        stm = {}
        stm_str = "chunk"
        f = open("Maude-2/results.txt", "r")
        i = 0
        for line in f:
            i += 1
            if stm_str in line:
                new_line = str(line)
                #print(new_line.find("goal"))
                if new_line.find("goal") != -1:
                    continue
                start = new_line.find("chunk ")+len("chunk ")
                end = new_line.find(" decay")
                mid = new_line[start:end]
                start_t = new_line.find("decay ")+len("decay ")
                end_t = new_line.find(" of")
                time = new_line[start_t:end_t]
                stm[mid] = time
        f.close()
        return stm

    def get_res_time(self):
        time_str = "in time"
        f = open("Maude-2/results.txt", "r")
        i = 0
        for line in f:
            i += 1
            if time_str in line:
                new_line = str(line)
                start = new_line.find("} ")+len("} ")
                end = new_line.find("\nBye")
                mid = new_line[start:end]
        f.close()
        return mid

    def get_res_ans(self):
        ans = {}
        ans_str = "ans"
        f = open("Maude-2/results.txt", "r")
        i = 0
        for line in f:
            i += 1
            if ans_str in line:
                cur_line = str(line)
                start = cur_line.find("(")+len("(")
                end = cur_line.rfind("\"")
                item = cur_line[start:end+1]
                start_t = cur_line.rfind("\" ") + len("\" ")
                end_t = cur_line.find("for")
                time = cur_line[start_t:end_t]
                ans[item] = time
        f.close()
        return ans

    def show_res(self):
        self.QAResultsWindow = QtWidgets.QMainWindow()
        self.ui = Ui_QAResWindow()
        self.ui.setupUi(self.QAResultsWindow)
        self.ui.label_2.setText(self.label.text())
        self.ui.label_3.setText(self.label_2.text())
        self.ui.version_id.setText(self.version_id.text())

        questions = self.get_questions()
        res_stm = self.get_res_stm()
        in_time = self.get_res_time()
        ans = self.get_res_ans()
        self.ui.label_6.setText(in_time)
        j=0
        for question in questions:
            self.ui.tableWidget.setRowCount(j+1)
            
            for item, time in ans.items():
                cat = item.split(' ', 3)[1][1:-1]
                attr = item.rsplit(' ', 1)[1][1:-1]

                # if question[4] in item and question[5] in item and question[6] in item:
                if question[4]==cat and question[6]==attr:
                    self.ui.tableWidget.setItem(j, 1, QtWidgets.QTableWidgetItem(item))
                    self.ui.tableWidget.setItem(j, 2, QtWidgets.QTableWidgetItem(time))
                    self.ui.tableWidget.setItem(j, 0, QtWidgets.QTableWidgetItem(str(question[5]+' a "'+question[4]+'" "'+question[6]+'" ?')))
                    self.ui.tableWidget.setItem(j, 0, QtWidgets.QTableWidgetItem(str(question[3])))
                    j += 1
            # q = self.ui.tableWidget.item(j,1);
            # for item, time in res_stm.items():
            #     if q:
            #         if "?" in item and question[4] in item and question[5] in item and question[6] in item:
            #             self.ui.tableWidget.setItem(j, 0, QtWidgets.QTableWidgetItem(item))
            # if not q:
            #     continue
            
        self.QAResultsWindow.show()

    def exp(self):
        self.ExperimentWindow = QtWidgets.QMainWindow()
        self.ui = Ui_ExperimentWindow()
        self.ui.setupUi(self.ExperimentWindow)
        self.ui.label_2.setText(self.label.text())
        self.ui.label_3.setText(self.label_2.text())
        self.ui.version_id.setText(self.version_id.text())
        self.ExperimentWindow.show()

    def env(self):
        self.EnvironmentWindow = QtWidgets.QMainWindow()
        self.ui = Ui_EnvironmentWindow()
        self.ui.setupUi(self.EnvironmentWindow)
        self.ui.label_2.setText(self.label.text())
        self.ui.label_3.setText(self.label_2.text())
        self.ui.version_id.setText(self.version_id.text())
        self.EnvironmentWindow.show()

    def short_term_mem(self):
        self.ShortTermMemWindow = QtWidgets.QMainWindow()
        self.ui = Ui_ShortTermMemWindow()
        self.ui.setupUi(self.ShortTermMemWindow)
        self.ui.label_2.setText(self.label.text())
        self.ui.label_3.setText(self.label_2.text())
        self.ui.version_id.setText(self.version_id.text())
        self.ShortTermMemWindow.show()

    def sem_mem(self):
        self.SemMemWindow = QtWidgets.QMainWindow()
        self.ui = Ui_SemMemWindow()
        self.ui.setupUi(self.SemMemWindow)
        self.ui.label_2.setText(self.label.text())
        self.ui.label_3.setText(self.label_2.text())
        self.ui.version_id.setText(self.version_id.text())
        self.SemMemWindow.show()

    def edit_database(self):
        self.DatabaseWindow = QtWidgets.QMainWindow()
        self.ui = Ui_DatabaseWindow()
        self.ui.setupUi(self.DatabaseWindow)
        self.ui.label_9.setText(self.label.text())
        self.ui.label_10.setText(self.label_2.text())
        self.ui.version_id.setText(self.version_id.text())
        self.DatabaseWindow.show()

    def exit_version(self):  
        reply = QMessageBox.question(self, "Exit version", "Do you want to save the changes?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            self.save_version()
        if reply == QMessageBox.No:
            return
        else:
            return

    def save_version(self):
        if self.version_number.text() == str(0):
            db = mdb.connect('127.0.0.1', 'root', '', 'interSys')
            with db:
                cur = db.cursor()
                ver_numb = float(1)

                self.CreateVersionInfoWindow = QtWidgets.QMainWindow()
                self.ui = Ui_CreateVersionInfoWindow()
                self.ui.setupUi(self.CreateVersionInfoWindow)
                self.ui.label_3.setText(self.project_name.text())
                self.ui.label_7.setText("Version " + str(ver_numb))
                self.ui.project_name.setText(self.project_name.text())
                self.ui.version_number.setText(str(ver_numb))
                self.CreateVersionInfoWindow.show()

     
                db.commit()
        else:
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
        self.label_0.setText(_translate("ProjectWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">Project Page</span></p></body></html>"))
        # self.label.setText(_translate("ProjectWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">Project: Animal-Dog</span></p></body></html>"))
        # self.label_2.setText(_translate("ProjectWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Version #1.1: Version Name 2</span></p></body></html>"))
        self.ExpBtn.setText(_translate("ProjectWindow", "Experiments"))
        self.learnBtn.setText(_translate("ProjectWindow", "Run Learning Process"))
        self.editDatabaseBtn.setText(_translate("ProjectWindow", "Edit Database"))
        self.runBtn.setText(_translate("ProjectWindow", "Run Experiment"))
        self.resultsBtn.setText(_translate("ProjectWindow", "Results"))
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

