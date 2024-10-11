# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from src.Controllers.UserController import *
from src.Views.adminwindow import Ui_adminWindow

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(879, 558)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.Title_login = QtWidgets.QTextBrowser(self.centralwidget)
        self.Title_login.setGeometry(QtCore.QRect(220, 30, 391, 71))
        self.Title_login.setObjectName("Title_login")
        self.login = QtWidgets.QTextEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(40, 140, 291, 41))
        self.login.setObjectName("login")
        self.password = QtWidgets.QTextEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(500, 140, 291, 41))
        self.password.setObjectName("password")
        self.loginbutton = QtWidgets.QPushButton(self.centralwidget)
        self.loginbutton.setGeometry(QtCore.QRect(290, 310, 251, 101))
        self.loginbutton.setObjectName("loginbutton")
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 879, 23))
        self.menubar.setObjectName("menubar")
        Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.Title_login.setHtml(_translate("Login", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Приветствуем Вас в информационной системе КАФЕ</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Пожалуйста введите свой логин и пароль</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.login.setHtml(_translate("Login", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.login.setPlaceholderText(_translate("Login", "Введите свой логин "))
        self.password.setHtml(_translate("Login", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.password.setPlaceholderText(_translate("Login", "Введите свой пароль "))
        self.loginbutton.setText(_translate("Login", "Войти"))

    def test_button(self):
        log = self.login.toPlainText()
        passwd = self.password.toPlainText()
        user = UserController()
        result = user.log_in(log,passwd)
        print(result)

    def pressButton(self):
        self.loginbutton.clicked.connect(self.open_panel)

    def open_panel(self):
        log = self.login.toPlainText()
        passwd = self.password.toPlainText()
        users = UserController()
        if users.log_in(log,passwd):
            if UserController.show(log).role_id.id == 1:
                print("Admin")
            elif UserController.show(log).role_id.id == 2:
                print("Cook")
            else:
                print("Oficiant")
        else:
            print("Пароль или логин введены не верно")


    def panel_admin(self):
        adminWindow = QtWidgets.QMainWindow()
        ui = Ui_adminWindow()
        ui.setupUi(adminWindow)
        adminWindow.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    ui.pressButton()
    sys.exit(app.exec_())
