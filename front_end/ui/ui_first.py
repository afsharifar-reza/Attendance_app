# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'first.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 669)
        MainWindow.setMinimumSize(QSize(450, 669))
        MainWindow.setMaximumSize(QSize(450, 669))
        MainWindow.setStyleSheet(u"QMainWindow{\n"
" background-color: rgb(254, 248, 226); ;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(130, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pic_main = QLabel(self.frame)
        self.pic_main.setObjectName(u"pic_main")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pic_main.sizePolicy().hasHeightForWidth())
        self.pic_main.setSizePolicy(sizePolicy)
        self.pic_main.setMaximumSize(QSize(400, 500))
        self.pic_main.setPixmap(QPixmap(u"../picture/logo.png"))
        self.pic_main.setScaledContents(True)
        self.pic_main.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.pic_main)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"B Titr"])
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.reg_btn = QPushButton(self.widget)
        self.reg_btn.setObjectName(u"reg_btn")
        self.reg_btn.setStyleSheet(u"QPushButton {\n"
"  padding: 6px 12px;\n"
"  font-size: 16px;\n"
"  font-weight: bold;\n"
"  color: #ffffff;\n"
"  background-color: #4CAF50; /* \u0633\u0628\u0632 */\n"
"  border: none;\n"
"  border-radius: 8px;\n"
"  cursor: pointer;\n"
"  transition: all 0.3s ease; /* \u0627\u0646\u06cc\u0645\u06cc\u0634\u0646 \u0646\u0631\u0645 \u0628\u0631\u0627\u06cc \u062a\u063a\u06cc\u06cc\u0631\u0627\u062a */\n"
"  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* \u0633\u0627\u06cc\u0647 */\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #45a049; /* \u0633\u0628\u0632 \u062a\u06cc\u0631\u0647\u200c\u062a\u0631 \u0647\u0646\u06af\u0627\u0645 hover */\n"
"  color: #000;\n"
"  transform: translateY(-2px); /* \u062d\u0631\u06a9\u062a \u062c\u0632\u0626\u06cc \u0628\u0647 \u0628\u0627\u0644\u0627 */\n"
"  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.reg_btn)

        self.login_btn = QPushButton(self.widget)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setLayoutDirection(Qt.LeftToRight)
        self.login_btn.setStyleSheet(u"QPushButton {\n"
"  padding: 6px 12px;\n"
"  font-size: 16px;\n"
"  font-weight: bold;\n"
"  color: #ffffff;\n"
"  background-color: #4CAF50; /* \u0633\u0628\u0632 */\n"
"  border: none;\n"
"  border-radius: 8px;\n"
"  cursor: pointer;\n"
"  transition: all 0.3s ease; /* \u0627\u0646\u06cc\u0645\u06cc\u0634\u0646 \u0646\u0631\u0645 \u0628\u0631\u0627\u06cc \u062a\u063a\u06cc\u06cc\u0631\u0627\u062a */\n"
"  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* \u0633\u0627\u06cc\u0647 */\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #45a049; /* \u0633\u0628\u0632 \u062a\u06cc\u0631\u0647\u200c\u062a\u0631 \u0647\u0646\u06af\u0627\u0645 hover */\n"
"  color: #000;\n"
"  transform: translateY(-2px); /* \u062d\u0631\u06a9\u062a \u062c\u0632\u0626\u06cc \u0628\u0647 \u0628\u0627\u0644\u0627 */\n"
"  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.login_btn)


        self.verticalLayout.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.frame)

        self.horizontalSpacer_2 = QSpacerItem(129, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 450, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pic_main.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0647 \u0633\u06cc\u0633\u062a\u0645 \u0627\u0637\u0644\u0627\u0639 \u0631\u0633\u0627\u0646\u06cc \u0647\u0646\u0631\u0633\u062a\u0627\u0646 \u062e\u0648\u0627\u0646\u0633\u0627\u0631\u06cc \u062e\u0648\u0634 \u0622\u0645\u062f\u06cc\u062f!", None))
        self.reg_btn.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u0646\u0627\u0645 ", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"\u0648\u0631\u0648\u062f ", None))
    # retranslateUi

