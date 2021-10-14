# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_screenXtVdGX.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(484, 595)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.skills_list_area = QFrame(self.centralwidget)
        self.skills_list_area.setObjectName(u"skills_list_area")
        self.skills_list_area.setGeometry(QRect(0, 0, 181, 581))
        self.skills_list_area.setFrameShape(QFrame.StyledPanel)
        self.skills_list_area.setFrameShadow(QFrame.Raised)
        self.scrollArea = QScrollArea(self.skills_list_area)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 49, 181, 521))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 162, 519))
        self.skf_1 = QFrame(self.scrollAreaWidgetContents)
        self.skf_1.setObjectName(u"skf_1")
        self.skf_1.setGeometry(QRect(0, 0, 161, 91))
        self.skf_1.setFrameShape(QFrame.StyledPanel)
        self.skf_1.setFrameShadow(QFrame.Raised)
        self.skf_1_title = QLabel(self.skf_1)
        self.skf_1_title.setObjectName(u"skf_1_title")
        self.skf_1_title.setGeometry(QRect(10, 10, 49, 16))
        font = QFont()
        font.setPointSize(12)
        self.skf_1_title.setFont(font)
        self.skf_1_start = QPushButton(self.skf_1)
        self.skf_1_start.setObjectName(u"skf_1_start")
        self.skf_1_start.setGeometry(QRect(10, 30, 141, 24))
        self.skf_1_include = QRadioButton(self.skf_1)
        self.skf_1_include.setObjectName(u"skf_1_include")
        self.skf_1_include.setGeometry(QRect(20, 60, 121, 20))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.skills_list_area_title = QLabel(self.skills_list_area)
        self.skills_list_area_title.setObjectName(u"skills_list_area_title")
        self.skills_list_area_title.setGeometry(QRect(10, 10, 161, 31))
        font1 = QFont()
        font1.setPointSize(15)
        self.skills_list_area_title.setFont(font1)
        self.practice_button = QPushButton(self.skills_list_area)
        self.practice_button.setObjectName(u"practice_button")
        self.practice_button.setGeometry(QRect(80, 10, 75, 31))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(180, 0, 16, 571))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lesson_title = QLabel(self.centralwidget)
        self.lesson_title.setObjectName(u"lesson_title")
        self.lesson_title.setGeometry(QRect(200, 15, 151, 21))
        self.lesson_title.setFont(font1)
        self.lesson_area = QFrame(self.centralwidget)
        self.lesson_area.setObjectName(u"lesson_area")
        self.lesson_area.setGeometry(QRect(200, 50, 261, 521))
        self.lesson_area.setFrameShape(QFrame.StyledPanel)
        self.lesson_area.setFrameShadow(QFrame.Raised)
        self.lesson_text = QLabel(self.lesson_area)
        self.lesson_text.setObjectName(u"lesson_text")
        self.lesson_text.setEnabled(True)
        self.lesson_text.setGeometry(QRect(20, 40, 221, 111))
        self.lesson_text.setLayoutDirection(Qt.LeftToRight)
        self.lesson_text.setFrameShape(QFrame.Box)
        self.lesson_text.setTextFormat(Qt.PlainText)
        self.lesson_text.setScaledContents(True)
        self.lesson_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.pushButton = QPushButton(self.lesson_area)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 250, 81, 31))
        font2 = QFont()
        font2.setPointSize(10)
        self.pushButton.setFont(font2)
        self.plainTextEdit = QPlainTextEdit(self.lesson_area)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(20, 160, 221, 71))
        self.label = QLabel(self.lesson_area)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 121, 16))
        font3 = QFont()
        font3.setPointSize(11)
        self.label.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.skf_1_title.setText(QCoreApplication.translate("MainWindow", u"Intro", None))
        self.skf_1_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.skf_1_include.setText(QCoreApplication.translate("MainWindow", u"Include in Practice", None))
        self.skills_list_area_title.setText(QCoreApplication.translate("MainWindow", u"Skills", None))
        self.practice_button.setText(QCoreApplication.translate("MainWindow", u"Practice", None))
        self.lesson_title.setText(QCoreApplication.translate("MainWindow", u"Select Lesson", None))
        self.lesson_text.setText(QCoreApplication.translate("MainWindow", u"ajwefojaiwojefioajwoefjioaweifjiaowejofjawiejfaiwejfoawfijew", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Result of Previous:", None))
    # retranslateUi
