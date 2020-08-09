# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
import sys
import os
import numpy as np
from Problem import Problem
import shutil

ROOT_DIR = './data'
JUDGE_DIR = os.path.join(ROOT_DIR, 'judgement')
MULTIPLE_CHOICE_DIR = os.path.join(ROOT_DIR, 'multiple_choice')

TEMP_DIR = './data/.temp'
TEMP_JUDGE_DIR = os.path.join(TEMP_DIR, 'judgement')
TEMP_MULTIPLE_CHOICE_DIR = os.path.join(TEMP_DIR, 'multiple_choice')

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1119, 827)
        Form.setStyleSheet("background-color: rgb(242, 255, 254);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(410, 30, 301, 141))
        self.label.setStyleSheet("background-color: rgb(236, 255, 221);")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(110, 180, 891, 361))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(110, 570, 891, 81))
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 710, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 710, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 710, 131, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(870, 710, 131, 41))
        self.pushButton_4.setObjectName("pushButton_4")

        # plots
        self.problem = None
        self.pushButton.clicked.connect(lambda: self.__get_judgement())
        self.pushButton_2.clicked.connect(lambda: self.__get_multiple_choice())
        self.pushButton_3.clicked.connect(lambda: self.__reset())
        self.pushButton_4.clicked.connect(lambda: self._show_answer())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:36pt;\">答题软件</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "下一判断题"))
        self.pushButton_2.setText(_translate("Form", "下一选择题"))
        self.pushButton_3.setText(_translate("Form", "清除题库"))
        self.pushButton_4.setText(_translate("Form", "显示答案"))

    def _show_question(self, problem):
        self.textBrowser.clear()
        self.textBrowser_2.clear()
        self.textBrowser.append(problem.get_question())

    def _show_answer(self):
        if self.problem is None:
            return
        self.textBrowser_2.clear()
        self.textBrowser_2.append(self.problem.get_answer())

    def __reset(self):
        # 重置题库
        li = os.listdir(TEMP_JUDGE_DIR)
        for filename in li:
            shutil.move(os.path.join(TEMP_JUDGE_DIR, filename), JUDGE_DIR)

        li = os.listdir(TEMP_MULTIPLE_CHOICE_DIR)
        for filename in li:
            shutil.move(os.path.join(TEMP_MULTIPLE_CHOICE_DIR, filename), MULTIPLE_CHOICE_DIR)

        self.textBrowser.clear()
        self.textBrowser_2.clear()

    def __get_judgement(self):
        li = os.listdir(JUDGE_DIR)

        # 题库空了
        if len(li) == 0:
            self.problem = None
            self.textBrowser.clear()
            self.textBrowser_2.clear()
            self.textBrowser.append('题库空了，重置题库或许可以帮到你')
            return

        # 题库未空，随机抽取
        index = np.random.randint(len(li))
        path = os.path.join(JUDGE_DIR, li[index])
        problem = Problem(path)
        shutil.move(path, os.path.join(TEMP_JUDGE_DIR, li[index]))
        self._show_question(problem)
        self.problem = problem

    def __get_multiple_choice(self):
        li = os.listdir(MULTIPLE_CHOICE_DIR)

        # 题库空了
        if len(li) == 0:
            self.problem = None
            self.textBrowser.clear()
            self.textBrowser_2.clear()
            self.textBrowser.append('题库空了，重置题库或许可以帮到你')
            return

        # 题库未空，随机抽取
        index = np.random.randint(len(li))
        path = os.path.join(MULTIPLE_CHOICE_DIR, li[index])
        problem = Problem(path)
        shutil.move(path, os.path.join(TEMP_MULTIPLE_CHOICE_DIR, li[index]))
        self._show_question(problem)
        self.problem = problem


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(w)
    ui.retranslateUi(w)
    w.show()

    sys.exit(app.exec_())
