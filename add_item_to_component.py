# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_to_sem_mem.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from functions_with_db import get_domains, get_facts, get_questions, get_fact, add_fact_to_exp, get_question, \
    add_quest_to_exp, add_fact_to_stm, add_quest_to_stm, add_fact_to_env, add_quest_to_env

add_fact = False

class Ui_AddItemToComponent(object):
    def setupUi(self, AddItemToComponent):
        AddItemToComponent.setObjectName("AddItemToComponent")
        AddItemToComponent.resize(513, 600)
        AddItemToComponent.setFixedSize(600, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddItemToComponent.sizePolicy().hasHeightForWidth())
        AddItemToComponent.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(AddItemToComponent)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 591, 51))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 1161, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(190, 520, 241, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.saveBtn.setFont(font)
        self.saveBtn.setObjectName("saveBtn")
        self.DomComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.DomComboBox.setGeometry(QtCore.QRect(220, 210, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DomComboBox.setFont(font)
        self.DomComboBox.setObjectName("DomComboBox")
        self.FactsComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.FactsComboBox.setGeometry(QtCore.QRect(220, 260, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FactsComboBox.setFont(font)
        self.FactsComboBox.setObjectName("FactsComboBox")
        self.QuestComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.QuestComboBox.setGeometry(QtCore.QRect(220, 260, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.QuestComboBox.setFont(font)
        self.QuestComboBox.setObjectName("QuestComboBox")
        self.factBtn = QtWidgets.QRadioButton(self.centralwidget)
        self.factBtn.setGeometry(QtCore.QRect(30, 110, 331, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.factBtn.setFont(font)
        self.factBtn.setObjectName("factBtn")
        self.buttonGroup = QtWidgets.QButtonGroup(AddItemToComponent)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.factBtn)
        self.questBtn = QtWidgets.QRadioButton(self.centralwidget)
        self.questBtn.setGeometry(QtCore.QRect(30, 140, 331, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.questBtn.setFont(font)
        self.questBtn.setObjectName("questBtn")
        self.buttonGroup.addButton(self.questBtn)
        self.for_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.for_lineEdit.setGeometry(QtCore.QRect(220, 360, 311, 41))
        self.for_lineEdit.setObjectName("for_lineEdit")
        self.in_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.in_lineEdit.setGeometry(QtCore.QRect(220, 310, 311, 41))
        self.in_lineEdit.setObjectName("in_lineEdit")
        self.repeat_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.repeat_lineEdit.setGeometry(QtCore.QRect(220, 410, 311, 41))
        self.repeat_lineEdit.setObjectName("repeat_lineEdit")
        self.in_time_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.in_time_lineEdit.setGeometry(QtCore.QRect(220, 460, 311, 41))
        self.in_time_lineEdit.setObjectName("in_time_lineEdit")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 360, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 310, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_repeat = QtWidgets.QLabel(self.centralwidget)
        self.label_repeat.setGeometry(QtCore.QRect(30, 410, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_repeat.setFont(font)
        self.label_repeat.setObjectName("label_repeat")
        self.label_in_time = QtWidgets.QLabel(self.centralwidget)
        self.label_in_time.setGeometry(QtCore.QRect(30, 460, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_in_time.setFont(font)
        self.label_in_time.setObjectName("label_in_time")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 260, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 260, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.decay_time_label = QtWidgets.QLabel(self.centralwidget)
        self.decay_time_label.setGeometry(QtCore.QRect(30, 310, 201, 31))
        self.decay_time_label.setFont(font)
        self.decay_time_label.setObjectName("decay_time_label")
        self.decay_time_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.decay_time_lineEdit.setGeometry(QtCore.QRect(220, 310, 311, 41))
        self.decay_time_lineEdit.setObjectName("decay_time_lineEdit")
        self.persistence_time_label = QtWidgets.QLabel(self.centralwidget)
        self.persistence_time_label.setGeometry(QtCore.QRect(30, 310, 201, 31))
        self.persistence_time_label.setFont(font)
        self.persistence_time_label.setObjectName("persistence_time_label")
        self.persistence_time_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.persistence_time_lineEdit.setGeometry(QtCore.QRect(220, 310, 311, 41))
        self.persistence_time_lineEdit.setObjectName("persistence_time_lineEdit")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(390, 110, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startBtn.setFont(font)
        self.startBtn.setObjectName("startBtn")
        AddItemToComponent.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddItemToComponent)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 513, 22))
        self.menubar.setObjectName("menubar")
        self.menuInteractive_System_Modelling = QtWidgets.QMenu(self.menubar)
        self.menuInteractive_System_Modelling.setObjectName("menuInteractive_System_Modelling")
        AddItemToComponent.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddItemToComponent)
        self.statusbar.setObjectName("statusbar")
        AddItemToComponent.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuInteractive_System_Modelling.menuAction())
        self.component = ''

        self.retranslateUi(AddItemToComponent)
        QtCore.QMetaObject.connectSlotsByName(AddItemToComponent)

        self.for_lineEdit.hide()
        self.in_lineEdit.hide()
        self.repeat_lineEdit.hide()
        self.in_time_lineEdit.hide()
        self.decay_time_lineEdit.hide()
        self.persistence_time_lineEdit.hide()
        self.FactsComboBox.hide()
        self.QuestComboBox.hide()
        self.DomComboBox.hide()

        self.label_8.hide()
        self.label_11.hide()
        self.label_9.hide()
        self.label_10.hide()
        self.label_4.hide()
        self.label_repeat.hide()
        self.label_in_time.hide()
        self.decay_time_label.hide()
        self.persistence_time_label.hide()

        self.version_id = QtWidgets.QLabel(self.centralwidget)
        self.version_id.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.version_id.setObjectName("version_id")

        self.startBtn.clicked.connect(self.startNow)
        self.saveBtn.clicked.connect(self.saveItem)
        self.saveBtn.clicked.connect(AddItemToComponent.close)

    def startNow(self):
        version_id = int(self.version_id.text())
        domains = get_domains(version_id)
        for x in domains:
            self.DomComboBox.addItem(x[2])
        self.factBtn.clicked.connect(self.addFact)
        self.questBtn.clicked.connect(self.addQuestion)

    def addFact(self):
        self.QuestComboBox.hide()
        self.DomComboBox.show()
        self.FactsComboBox.show()
        self.label_10.hide()
        self.label_9.show()
        self.label_4.show()
        self.FactsComboBox.clear()
        self.QuestComboBox.clear()
        if self.component == "experiment":
            self.for_lineEdit.show()
            self.in_lineEdit.show()
            self.repeat_lineEdit.show()
            self.in_time_lineEdit.show()
            self.label_8.show()
            self.label_11.show()
            self.label_repeat.show()
            self.label_in_time.show()
        if self.component == "short_term_mem":
            self.decay_time_lineEdit.show()
            self.decay_time_label.show()
        if self.component == "environment":
            self.persistence_time_lineEdit.show()
            self.persistence_time_label.show()
        global add_fact
        add_fact = True
        version_id = int(self.version_id.text())
        facts = get_facts(version_id)
        for x in facts:
            self.FactsComboBox.addItem(x[2])

    def addQuestion(self):
        self.FactsComboBox.hide()
        self.DomComboBox.show()
        self.QuestComboBox.show()
        self.label_9.hide()
        self.label_10.show()
        self.label_4.show()
        self.FactsComboBox.clear()
        self.QuestComboBox.clear()
        if self.component == "experiment":
            self.for_lineEdit.show()
            self.in_lineEdit.show()
            self.repeat_lineEdit.hide()
            self.in_time_lineEdit.hide()
            self.label_repeat.hide()
            self.label_in_time.hide()
            self.label_8.show()
            self.label_11.show()
        if self.component == "short_term_mem":
            self.decay_time_lineEdit.show()
            self.decay_time_label.show()
        if self.component == "environment":
            self.persistence_time_lineEdit.show()
            self.persistence_time_label.show()
        global add_fact
        add_fact = False
        version_id = int(self.version_id.text())
        questions = get_questions(version_id)
        for x in questions:
            self.QuestComboBox.addItem(x[2])

    def saveItem(self):
        version_id = int(self.version_id.text())
        cur_dom = str(self.DomComboBox.currentText())
        global add_fact
        if(add_fact):
            add_fact = False
            cur_fact = str(self.FactsComboBox.currentText())
            facts = get_fact(version_id, cur_fact)
            print(facts)
            for fact in facts:
                fact_cat = fact[3]
                fact_type = fact[4]
                fact_attr = fact[5]
            if self.component == 'experiment':
                cur_for_time = int(str(self.for_lineEdit.text()))
                cur_in_time = int(str(self.in_lineEdit.text()))
                repeat = int(str(self.repeat_lineEdit.text()))
                repeat_in_time = int(str(self.in_time_lineEdit.text()))
                params = [version_id, cur_dom, cur_fact, cur_in_time, cur_for_time, fact_cat, fact_type, fact_attr, repeat, repeat_in_time]
                add_fact_to_exp(params)
            elif self.component == "short_term_mem":
                cur_decay = int(str(self.decay_time_lineEdit.text()))
                params = [version_id, cur_dom, cur_fact, cur_decay, fact_cat, fact_type, fact_attr]
                add_fact_to_stm(params)
            elif self.component == "environment":
                cur_persist_time = int(str(self.persistence_time_lineEdit.text()))
                params = [version_id, cur_dom, cur_fact, cur_persist_time, fact_cat, fact_type, fact_attr]
                add_fact_to_env(params)
        else:
            cur_quest = str(self.QuestComboBox.currentText())
            questions = get_question(version_id, cur_quest)
            for quest in questions:
                quest_cat = quest[4]
                quest_type = quest[3]
                quest_attr = quest[5]
            if self.component == 'experiment':
                cur_for_time = int(str(self.for_lineEdit.text()))
                cur_in_time = int(str(self.in_lineEdit.text()))
                params = [version_id, cur_dom, cur_quest, cur_in_time, cur_for_time, quest_cat, quest_type, quest_attr]
                add_quest_to_exp(params)
            elif self.component == "short_term_mem":
                cur_decay = int(str(self.decay_time_lineEdit.text()))
                params = [version_id, cur_dom, cur_quest, cur_decay, quest_cat, quest_type, quest_attr]
                add_quest_to_stm(params)
            elif self.component == "environment":
                cur_persist_time = int(str(self.persistence_time_lineEdit.text()))
                params = [version_id, cur_dom, cur_quest, cur_persist_time, quest_cat, quest_type, quest_attr]
                add_quest_to_env(params)
        QtWidgets.QMessageBox.about(self.centralwidget,'Connection', 'Data Inserted Successfully')



    def retranslateUi(self, AddItemToComponent):
        _translate = QtCore.QCoreApplication.translate
        AddItemToComponent.setWindowTitle(_translate("AddItemToComponent", "MainWindow"))
        self.label.setText(_translate("AddItemToComponent", "<html><head/><body><p><span style=\" font-size:28pt;\">Add Item Representation</span></p></body></html>"))
        self.saveBtn.setText(_translate("AddItemToComponent", "Save"))
        self.DomComboBox.setItemText(0, _translate("AddItemToComponent", "Animals"))
        self.DomComboBox.setItemText(1, _translate("AddItemToComponent", "Dogs"))
        self.FactsComboBox.setItemText(0, _translate("AddItemToComponent", "Animal can breath"))
        self.FactsComboBox.setItemText(1, _translate("AddItemToComponent", "Animal can move"))
        self.factBtn.setText(_translate("AddItemToComponent", "Add fact"))
        self.questBtn.setText(_translate("AddItemToComponent", "Add question"))
        self.label_4.setText(_translate("AddItemToComponent", "Domain"))
        self.label_9.setText(_translate("AddItemToComponent", "Fact"))
        self.label_10.setText(_translate("AddItemToComponent", "Question"))

        self.startBtn.setText(_translate("EditDatabaseItemWindow", "Start"))
        self.menuInteractive_System_Modelling.setTitle(_translate("AddItemToComponent", "1"))

