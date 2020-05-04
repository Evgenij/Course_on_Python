# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Evgenij\Python\Lab_3\Task5\window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from string_formatter import StringFormatter

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 370)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label.setObjectName("label")
        self.fieldString = QtWidgets.QLineEdit(MainWindow)
        self.fieldString.setGeometry(QtCore.QRect(10, 30, 301, 20))
        self.fieldString.setObjectName("field_string")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(10, 320, 71, 16))
        self.label_2.setObjectName("label_2")
        self.fieldResult = QtWidgets.QLineEdit(MainWindow)
        self.fieldResult.setGeometry(QtCore.QRect(10, 340, 301, 20))
        self.fieldResult.setObjectName("field_result")
        self.button = QtWidgets.QPushButton(MainWindow)
        self.button.setGeometry(QtCore.QRect(150, 260, 151, 31))
        self.button.setObjectName("button")
        self.delete_wordsCheck = QtWidgets.QCheckBox(MainWindow)
        self.delete_wordsCheck.setGeometry(QtCore.QRect(20, 90, 201, 17))
        self.delete_wordsCheck.setObjectName("delete_words_check")
        self.replacementCheck = QtWidgets.QCheckBox(MainWindow)
        self.replacementCheck.setGeometry(QtCore.QRect(20, 140, 151, 17))
        self.replacementCheck.setObjectName("replacement_check")
        self.spacesCheck = QtWidgets.QCheckBox(MainWindow)
        self.spacesCheck.setGeometry(QtCore.QRect(20, 160, 205, 17))
        self.spacesCheck.setObjectName("spaces_check")
        self.sorting = QtWidgets.QCheckBox(MainWindow)
        self.sorting.setGeometry(QtCore.QRect(20, 180, 171, 17))
        self.sorting.setObjectName("sorting")
        self.sort_lenghtCheck = QtWidgets.QRadioButton(MainWindow)
        self.sort_lenghtCheck.setGeometry(QtCore.QRect(40, 200, 82, 17))
        self.sort_lenghtCheck.setObjectName("sort_lenght_check")
        self.sort_lexCheck = QtWidgets.QRadioButton(MainWindow)
        self.sort_lexCheck.setGeometry(QtCore.QRect(40, 220, 131, 17))
        self.sort_lexCheck.setObjectName("sort_lex_check")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 151, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(160, 60, 151, 16))
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(MainWindow)
        self.spinBox.setGeometry(QtCore.QRect(40, 110, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(90, 120, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(MainWindow)
        self.label_6.setGeometry(QtCore.QRect(10, 290, 301, 20))
        self.label_6.setObjectName("label_6")

        self.sf = StringFormatter()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лаб №3 задание №5 "))
        self.label.setText(_translate("MainWindow", "Строка"))
        self.label_2.setText(_translate("MainWindow", "Результат"))
        self.button.setText(_translate("MainWindow", "Форматировать"))
        self.button.clicked.connect(self.button_Clicked)
        self.delete_wordsCheck.setText(_translate("MainWindow", "Удалить слова размером меньше ..."))
        self.replacementCheck.setText(_translate("MainWindow", "Заменить все цифры на *"))
        self.spacesCheck.setText(_translate("MainWindow", "Вставить пробелы между символами"))
        self.sorting.setText(_translate("MainWindow", "Сортировать слова в строке"))
        self.sorting.clicked.connect(self.sorting_Clicked)
        self.sort_lenghtCheck.setText(_translate("MainWindow", "По длинне"))
        self.sort_lenghtCheck.setEnabled(False)
        self.sort_lexCheck.setText(_translate("MainWindow", "Лексикографически"))
        self.sort_lexCheck.setEnabled(False)
        self.label_3.setText(_translate("MainWindow", "Параметры форматирования"))
        self.label_4.setText(_translate("MainWindow", "________________________"))
        self.label_5.setText(_translate("MainWindow", "букв"))
        self.label_6.setText(_translate("MainWindow", "_________________________________________________"))

    def button_Clicked(self):
        self.sf.set_string(self.fieldString.text())
        self.fieldResult.setText(self.sf.formatting(self.delete_wordsCheck.isChecked(),
                                                    int(self.spinBox.text()),
                                                    self.replacementCheck.isChecked(),
                                                    self.spacesCheck.isChecked(),
                                                    self.sort_lenghtCheck.isChecked(),
                                                    self.sort_lexCheck.isChecked()))

    def sorting_Clicked(self):
        if self.sorting.isChecked() == True:
            self.sort_lenghtCheck.setCheckable(True)
            self.sort_lexCheck.setCheckable(True)
            self.sort_lenghtCheck.setEnabled(True)
            self.sort_lexCheck.setEnabled(True)
        else:
            self.sort_lenghtCheck.setCheckable(False)
            self.sort_lexCheck.setCheckable(False)
            self.sort_lenghtCheck.setEnabled(False)
            self.sort_lexCheck.setEnabled(False)