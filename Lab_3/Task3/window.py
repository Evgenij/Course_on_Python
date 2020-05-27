# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Evgenij\Python\Python\Scripts\window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os
import re

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, QFileInfo
from PyQt5.QtWidgets import QFileDialog
from win32com.test.testPersist import now


class VLine(QtWidgets.QFrame):
    # a simple VLine, like the one you get from designer
    def __init__(self):
        super(VLine, self).__init__()
        self.setFrameShape(self.VLine|self.Sunken)

class Message(QtWidgets.QMainWindow):
    def Show(self):
        textMmessage = 'Вы действительно хотите открыть лог? Данные последних поисков будут потеряны!'
        reply = QtWidgets.QMessageBox.question(self, 'Открытие лога', textMmessage,
                                           QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            return 'yes'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 400)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralWidget")
        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, 0, 650, 359))
        self.listView.setObjectName("listView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 21))
        self.menubar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)

        self.labelFileName = QtWidgets.QLabel("Обработан файл: ")
        self.labelFileSize = QtWidgets.QLabel("")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusBar")
        self.statusbar.addPermanentWidget(self.labelFileName, 60)
        self.statusbar.addPermanentWidget(VLine())
        self.statusbar.addPermanentWidget(self.labelFileSize, 40)
        MainWindow.setStatusBar(self.statusbar)

        self.openFile = QtWidgets.QAction(MainWindow)
        self.openFile.setObjectName("openFile")
        self.closeApp = QtWidgets.QAction(MainWindow)
        self.closeApp.setObjectName("closeApp")
        self.exportLog = QtWidgets.QAction(MainWindow)
        self.exportLog.setObjectName("ExportLog")
        self.addToLog = QtWidgets.QAction(MainWindow)
        self.addToLog.setObjectName("AddToLog")
        self.readLog = QtWidgets.QAction(MainWindow)
        self.readLog.setObjectName("ReadLog")     
        self.menuFile.addAction(self.openFile)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.closeApp)
        self.menu.addAction(self.addToLog)
        self.menu.addAction(self.readLog)  
        self.menu.addAction(self.exportLog)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Обработчик файлов"))
        # -----properties
        self.menuFile.setTitle(_translate("MainWindow", "Файл"))
        self.menu.setTitle(_translate("MainWindow", "Лог"))
        self.openFile.setText(_translate("MainWindow", "Открыть"))
        self.closeApp.setText(_translate("MainWindow", "Выход"))
        self.exportLog.setText(_translate("MainWindow", "Экспорт"))
        self.addToLog.setText(_translate("MainWindow", "Добавить в лог"))
        self.readLog.setText(_translate("MainWindow", "Просмотр"))
        #-----events
        self.openFile.triggered.connect(self.OpenFile)
        self.closeApp.triggered.connect(QCoreApplication.instance().quit)
        self.exportLog.triggered.connect(self.ExportLog)
        self.addToLog.triggered.connect(self.AddToLog)
        self.readLog.triggered.connect(self.ReadLog)


    #открытие и обработка файла
    def OpenFile(self):
        fileName = QFileDialog.getOpenFileName()

        if fileName[0] != '':
            file = open(fileNam[0],'r')
            self.listView.addItem('Файл '+ file.name +' был обработан '+ now.strftime("%d.%m.%Y %H:%M") +':')
            self.listView.addItem("")

            #обработка файла
            text = [string.strip() for string in file.readlines()]
            pattern = re.compile('\d\d-\d\d-\d\d\d\d')
            dates = { }

            for index, string in enumerate(text):
                matches = pattern.finditer(string)
                for match in matches:
                    dates["Строка " + str(index + 1) + ", позиция " + str(
                        match.start())] = " : найдено '" + match.group() + "'"

            for key in dates.keys():
                self.listView.addItem(key + dates[key])

            self.listView.addItem("")
            self.labelFileName.setText('Обработан файл: {0}'.format(file.name))
            self.labelFileSize.setText(str(os.path.getsize(fileName[0])) + " байт")

    # добавление в пользовательский лог
    def ExportLog(self):
        fileName = QFileDialog.getSaveFileName()
        logfile = open(fileName[0] + '.log','w')

        if self.listView.count() != 0:
            for i in range(0,self.listView.count()):
                logfile.write(self.listView.item(i).text()+'\n')

        logfile.close()

    # добавление в системный лог
    def AddToLog(self):
        logfile = open('script18.log','a')
        if self.listView.count() != 0:
            for i in range(0,self.listView.count()):
                logfile.write(self.listView.item(i).text()+'\n')

        logfile.close()

    # просмотр лога
    def ReadLog(self):
        messageBox = Message()
        if messageBox.Show() == 'yes':
            self.listView.clear()

            fileName = QFileDialog.getOpenFileName()
            logfile = open(fileName[0], "r")
            self.labelFileName.setText('Открыт лог: {0}'.format(logfile.name))
            self.labelFileSize.setText(str(os.path.getsize(fileName[0])) + " байт")

            lines = logfile.readlines()
            for i in range(0,len(lines)):
                self.listView.addItem(lines[i][:-2])

            logfile.close()
