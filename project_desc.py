# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_desc.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProjectDescWindow(object):
    def setupUi(self, ProjectDescWindow):
        ProjectDescWindow.setObjectName("ProjectDescWindow")
        ProjectDescWindow.setFixedSize(553, 416)
        self.centralwidget = QtWidgets.QWidget(ProjectDescWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 591, 51))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 1161, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 130, 411, 192))
        self.textBrowser.setObjectName("textBrowser")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        ProjectDescWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ProjectDescWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 22))
        self.menubar.setObjectName("menubar")
        self.menuInteractive_System_Modelling = QtWidgets.QMenu(self.menubar)
        self.menuInteractive_System_Modelling.setObjectName("menuInteractive_System_Modelling")
        ProjectDescWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ProjectDescWindow)
        self.statusbar.setObjectName("statusbar")
        ProjectDescWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuInteractive_System_Modelling.menuAction())

        self.retranslateUi(ProjectDescWindow)
        QtCore.QMetaObject.connectSlotsByName(ProjectDescWindow)

    def retranslateUi(self, ProjectDescWindow):
        _translate = QtCore.QCoreApplication.translate
        ProjectDescWindow.setWindowTitle(_translate("ProjectDescWindow", "MainWindow"))
        self.label.setText(_translate("ProjectDescWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">Project Description</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("ProjectDescWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">This project This project This project This project This project This project This project This project This project This project </span></p></body></html>"))
        self.menuInteractive_System_Modelling.setTitle(_translate("ProjectDescWindow", "1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProjectDescWindow = QtWidgets.QMainWindow()
    ui = Ui_ProjectDescWindow()
    ui.setupUi(ProjectDescWindow)
    ProjectDescWindow.show()
    sys.exit(app.exec_())