# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget_dashboard = QStackedWidget(self.centralwidget)
        self.stackedWidget_dashboard.setObjectName(u"stackedWidget_dashboard")
        self.stackedWidget_dashboard.setStyleSheet(u"QStackedWidget{\n"
" background-color: #EAEFEF;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  border-radius: 8px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"\n"
"}")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.horizontalLayout_6 = QHBoxLayout(self.main_page)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame = QFrame(self.main_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 80))
        self.widget_2.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel{\n"
" background-color: #FFE3BB; \n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:15 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  color:#E14434;\n"
"\n"
"}\n"
"\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"B Mitra"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:15 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"}")

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 80))
        self.widget_3.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QLabel{\n"
" background-color: #FFE3BB; \n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:15 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  color:#E14434;\n"
"\n"
"}\n"
"\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:15 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_5)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.frame)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 80))
        self.widget_4.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"QLabel{\n"
" background-color: #FFE3BB; \n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:15 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  color:#E14434;\n"
"\n"
"}\n"
"\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"QLabel{\n"
" background-color:  #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:15 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_7)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.frame)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 80))
        self.widget_5.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"QLabel{\n"
" background-color: #FFE3BB; \n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:15 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  color:#E14434;\n"
"\n"
"}\n"
"\n"
"")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.label_9 = QLabel(self.widget_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 0))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"QLabel{\n"
" background-color:  #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:15 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_9)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.frame)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 120))
        self.widget_6.setMaximumSize(QSize(16777215, 120))
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName(u"label_10")
        font2 = QFont()
        font2.setFamilies([u"B Mitra"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_10)


        self.verticalLayout_2.addWidget(self.widget_6)


        self.horizontalLayout_6.addWidget(self.frame)

        self.stackedWidget_dashboard.addWidget(self.main_page)
        self.mange_page = QWidget()
        self.mange_page.setObjectName(u"mange_page")
        self.mange_page.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout_8 = QHBoxLayout(self.mange_page)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.mange_tab = QTabWidget(self.mange_page)
        self.mange_tab.setObjectName(u"mange_tab")
        self.mange_tab.setMinimumSize(QSize(0, 40))
        self.mange_tab.setLayoutDirection(Qt.RightToLeft)
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_5 = QSpacerItem(81, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.class_tableWidget = QTableWidget(self.tab_4)
        if (self.class_tableWidget.columnCount() < 3):
            self.class_tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.class_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.class_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.class_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.class_tableWidget.setObjectName(u"class_tableWidget")
        self.class_tableWidget.setMinimumSize(QSize(400, 400))
        self.class_tableWidget.setMaximumSize(QSize(400, 400))
        self.class_tableWidget.setStyleSheet(u"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u067e\u0627\u06cc\u0647 \u0628\u0631\u0627\u06cc \u062c\u062f\u0648\u0644 */\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 4px;\n"
"    font-family: Segoe UI, Arial, sans-serif;\n"
"    font-size: 12px;\n"
"    gridline-color: #f0f0f0;\n"
"    outline: 0;\n"
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u0622\u06cc\u062a\u0645\u200c\u0647\u0627\u06cc \u062c\u062f\u0648\u0644 */\n"
"QTableWidget::item {\n"
"    padding: 6px;\n"
"    border-bottom: 1px solid #f0f0f0;\n"
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u0622\u06cc\u062a\u0645\u200c\u0647\u0627\u06cc \u0627\u0646\u062a\u062e\u0627\u0628 \u0634\u062f\u0647 */\n"
"QTableWidget::item:selected {\n"
"    background-color: #4a90e2;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u0647\u062f\u0631\u0647\u0627\u06cc \u062c\u062f\u0648\u0644 */\n"
"QHeaderView::section {\n"
"    background-color: #f8f9fa;\n"
""
                        "    color: #495057;\n"
"    padding: 8px;\n"
"    border: none;\n"
"    font-weight: 500;\n"
"    text-align: left;\n"
"}\n"
"\n"
"/* \u0627\u0641\u06a9\u062a hover \u0631\u0648\u06cc \u0647\u062f\u0631\u0647\u0627 */\n"
"QHeaderView::section:hover {\n"
"    background-color: #e9ecef;\n"
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u06af\u0648\u0634\u0647 \u062c\u062f\u0648\u0644 (\u0645\u062d\u0644 \u062a\u0642\u0627\u0637\u0639 \u0647\u062f\u0631\u0647\u0627\u06cc \u0639\u0645\u0648\u062f\u06cc \u0648 \u0627\u0641\u0642\u06cc) */\n"
"QTableCornerButton::section {\n"
"    background-color: #f8f9fa;\n"
"    border: none;\n"
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u0627\u0633\u06a9\u0631\u0648\u0644 \u0628\u0627\u0631 \u0639\u0645\u0648\u062f\u06cc */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f8f9fa;\n"
"    width: 10px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #ced4da;\n"
"    min-height: 20px;\n"
"    border-radius: 5px"
                        ";\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"    background: none;\n"
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u0627\u0633\u06a9\u0631\u0648\u0644 \u0628\u0627\u0631 \u0627\u0641\u0642\u06cc (\u062f\u0631 \u0635\u0648\u0631\u062a \u0646\u06cc\u0627\u0632) */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #f8f9fa;\n"
"    height: 10px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #ced4da;\n"
"    min-width: 20px;\n"
"    border-radius: 5px;\n"
"}")
        self.class_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.class_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.class_tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_9.addWidget(self.class_tableWidget)

        self.horizontalSpacer_6 = QSpacerItem(81, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.mange_tab.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_12 = QHBoxLayout(self.tab)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget_7 = QWidget(self.tab)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 40))
        self.widget_7.setAutoFillBackground(True)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_11 = QLabel(self.widget_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(75, 40))
        self.label_11.setMaximumSize(QSize(80, 40))
        self.label_11.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_11)

        self.Grade_comboBox = QComboBox(self.widget_7)
        self.Grade_comboBox.addItem("")
        self.Grade_comboBox.addItem("")
        self.Grade_comboBox.addItem("")
        self.Grade_comboBox.setObjectName(u"Grade_comboBox")
        self.Grade_comboBox.setMinimumSize(QSize(0, 40))
        self.Grade_comboBox.setLayoutDirection(Qt.RightToLeft)
        self.Grade_comboBox.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.Grade_comboBox)

        self.label = QLabel(self.widget_7)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(75, 40))
        self.label.setMaximumSize(QSize(85, 40))
        self.label.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label)

        self.Field_comboBox = QComboBox(self.widget_7)
        self.Field_comboBox.addItem("")
        self.Field_comboBox.addItem("")
        self.Field_comboBox.addItem("")
        self.Field_comboBox.addItem("")
        self.Field_comboBox.setObjectName(u"Field_comboBox")
        self.Field_comboBox.setMinimumSize(QSize(0, 40))
        self.Field_comboBox.setAutoFillBackground(True)
        self.Field_comboBox.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.Field_comboBox)

        self.sub_btn = QPushButton(self.widget_7)
        self.sub_btn.setObjectName(u"sub_btn")

        self.horizontalLayout_7.addWidget(self.sub_btn)


        self.horizontalLayout_12.addWidget(self.widget_7)

        self.mange_tab.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_11 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.frame_2 = QFrame(self.tab_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(150, 0))
        self.label_12.setMaximumSize(QSize(150, 16777215))
        self.label_12.setLayoutDirection(Qt.LeftToRight)
        self.label_12.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_12)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(150, 0))
        self.label_13.setMaximumSize(QSize(150, 16777215))
        self.label_13.setLayoutDirection(Qt.LeftToRight)
        self.label_13.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_13)

        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(150, 0))
        self.label_14.setMaximumSize(QSize(150, 16777215))
        self.label_14.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_14)

        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(150, 0))
        self.label_15.setMaximumSize(QSize(150, 16777215))
        self.label_15.setLayoutDirection(Qt.LeftToRight)
        self.label_15.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_15)

        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(150, 0))
        self.label_16.setMaximumSize(QSize(150, 16777215))
        self.label_16.setLayoutDirection(Qt.LeftToRight)
        self.label_16.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_16)

        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(150, 0))
        self.label_17.setMaximumSize(QSize(150, 16777215))
        self.label_17.setLayoutDirection(Qt.LeftToRight)
        self.label_17.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_17)

        self.first_name_lineEdit = QLineEdit(self.frame_2)
        self.first_name_lineEdit.setObjectName(u"first_name_lineEdit")
        self.first_name_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0641\u0648\u0646\u062a \u0648 \u0645\u062a\u0646 */\n"
"    font-family: \"Segoe UI\", \"B Nazanin\", \"Arial\";\n"
"    font-size: 12px;\n"
"    color: #495057;\n"
"    \n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u062d\u0627\u0634\u06cc\u0647 \u0648 \u0641\u0627\u0635\u0644\u0647 */\n"
"    padding: 6px 8px;\n"
"    margin: 2px;\n"
"    \n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0638\u0627\u0647\u0631\u06cc */\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 4px;\n"
"    \n"
"    /* \u062c\u0644\u0648\u0647\u200c\u0647\u0627\u06cc \u0648\u06cc\u0698\u0647 */\n"
"    selection-background-color: #007bff;\n"
"    selection-color: #ffffff;\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.first_name_lineEdit)

        self.last_name_lineEdit = QLineEdit(self.frame_2)
        self.last_name_lineEdit.setObjectName(u"last_name_lineEdit")
        self.last_name_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0641\u0648\u0646\u062a \u0648 \u0645\u062a\u0646 */\n"
"    font-family: \"Segoe UI\", \"B Nazanin\", \"Arial\";\n"
"    font-size: 12px;\n"
"    color: #495057;\n"
"    \n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u062d\u0627\u0634\u06cc\u0647 \u0648 \u0641\u0627\u0635\u0644\u0647 */\n"
"    padding: 6px 8px;\n"
"    margin: 2px;\n"
"    \n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0638\u0627\u0647\u0631\u06cc */\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 4px;\n"
"    \n"
"    /* \u062c\u0644\u0648\u0647\u200c\u0647\u0627\u06cc \u0648\u06cc\u0698\u0647 */\n"
"    selection-background-color: #007bff;\n"
"    selection-color: #ffffff;\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.last_name_lineEdit)

        self.father_name_lineEdit = QLineEdit(self.frame_2)
        self.father_name_lineEdit.setObjectName(u"father_name_lineEdit")
        self.father_name_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0641\u0648\u0646\u062a \u0648 \u0645\u062a\u0646 */\n"
"    font-family: \"Segoe UI\", \"B Nazanin\", \"Arial\";\n"
"    font-size: 12px;\n"
"    color: #495057;\n"
"    \n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u062d\u0627\u0634\u06cc\u0647 \u0648 \u0641\u0627\u0635\u0644\u0647 */\n"
"    padding: 6px 8px;\n"
"    margin: 2px;\n"
"    \n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0638\u0627\u0647\u0631\u06cc */\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 4px;\n"
"    \n"
"    /* \u062c\u0644\u0648\u0647\u200c\u0647\u0627\u06cc \u0648\u06cc\u0698\u0647 */\n"
"    selection-background-color: #007bff;\n"
"    selection-color: #ffffff;\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.father_name_lineEdit)

        self.class_comboBox = QComboBox(self.frame_2)
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.setObjectName(u"class_comboBox")
        self.class_comboBox.setMinimumSize(QSize(202, 32))
        self.class_comboBox.setLayoutDirection(Qt.RightToLeft)
        self.class_comboBox.setStyleSheet(u"QComboBox {\n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0641\u0648\u0646\u062a */\n"
"    font-family: \"B Nazanin\", \"Segoe UI\", Arial;\n"
"    font-size: 13px;\n"
"    color: #495057;\n"
"    \n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0638\u0627\u0647\u0631\u06cc */\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 4px;\n"
"  \n"
"    min-width: 200px;\n"
"    min-height: 30px;\n"
"    \n"
"    /* \u062a\u0631\u0627\u0632 \u0645\u062a\u0646 \u0628\u0631\u0627\u06cc \u0641\u0627\u0631\u0633\u06cc - \u0631\u0627\u0647 \u062d\u0644 \u0627\u0635\u0644\u06cc */\n"
"    text-align: right;\n"
"    direction: rtl;\n"
"}\n"
"\n"
"/* \u0631\u0627\u0647\u06a9\u0627\u0631 \u062c\u0627\u06cc\u06af\u0632\u06cc\u0646 \u0628\u0631\u0627\u06cc \u062a\u0631\u0627\u0632 \u0645\u062a\u0646 */\n"
"QComboBox QAbstractItemView {\n"
"    text-align: right;\n"
"    direction: rtl;\n"
"}\n"
"\n"
"/* \u0639\u0646\u0635\u0631 \u0645\u062a\u0646 \u062f\u0627\u062e\u0644"
                        " \u06a9\u0627\u0645\u0628\u0648\u0628\u0627\u06a9\u0633 */\n"
"QComboBox QLineEdit {\n"
"    text-align: right;\n"
"    padding-right: 5px;\n"
"    direction: rtl;\n"
"}")
        self.class_comboBox.setMaxCount(2147483646)
        self.class_comboBox.setInsertPolicy(QComboBox.InsertAtBottom)
        self.class_comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.class_comboBox)

        self.parent_phone_lineEdit = QLineEdit(self.frame_2)
        self.parent_phone_lineEdit.setObjectName(u"parent_phone_lineEdit")
        self.parent_phone_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0641\u0648\u0646\u062a \u0648 \u0645\u062a\u0646 */\n"
"    font-family: \"Segoe UI\", \"B Nazanin\", \"Arial\";\n"
"    font-size: 12px;\n"
"    color: #495057;\n"
"    \n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u062d\u0627\u0634\u06cc\u0647 \u0648 \u0641\u0627\u0635\u0644\u0647 */\n"
"    padding: 6px 8px;\n"
"    margin: 2px;\n"
"    \n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0638\u0627\u0647\u0631\u06cc */\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 4px;\n"
"    \n"
"    /* \u062c\u0644\u0648\u0647\u200c\u0647\u0627\u06cc \u0648\u06cc\u0698\u0647 */\n"
"    selection-background-color: #007bff;\n"
"    selection-color: #ffffff;\n"
"}")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.parent_phone_lineEdit)

        self.student_id_lineEdit = QLineEdit(self.frame_2)
        self.student_id_lineEdit.setObjectName(u"student_id_lineEdit")
        self.student_id_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0641\u0648\u0646\u062a \u0648 \u0645\u062a\u0646 */\n"
"    font-family: \"Segoe UI\", \"B Nazanin\", \"Arial\";\n"
"    font-size: 12px;\n"
"    color: #495057;\n"
"    \n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u062d\u0627\u0634\u06cc\u0647 \u0648 \u0641\u0627\u0635\u0644\u0647 */\n"
"    padding: 6px 8px;\n"
"    margin: 2px;\n"
"    \n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0638\u0627\u0647\u0631\u06cc */\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 4px;\n"
"    \n"
"    /* \u062c\u0644\u0648\u0647\u200c\u0647\u0627\u06cc \u0648\u06cc\u0698\u0647 */\n"
"    selection-background-color: #007bff;\n"
"    selection-color: #ffffff;\n"
"}")
        self.student_id_lineEdit.setMaxLength(32765)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.student_id_lineEdit)


        self.verticalLayout_4.addLayout(self.formLayout)

        self.widget_8 = QWidget(self.frame_2)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.submit_student_btn = QPushButton(self.widget_8)
        self.submit_student_btn.setObjectName(u"submit_student_btn")

        self.horizontalLayout_10.addWidget(self.submit_student_btn)


        self.verticalLayout_4.addWidget(self.widget_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_11.addWidget(self.frame_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)

        self.mange_tab.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.mange_tab.addTab(self.tab_3, "")

        self.horizontalLayout_8.addWidget(self.mange_tab)

        self.stackedWidget_dashboard.addWidget(self.mange_page)

        self.horizontalLayout.addWidget(self.stackedWidget_dashboard)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(150, 0))
        self.widget.setMaximumSize(QSize(300, 16777215))
        self.widget.setStyleSheet(u"QWidget{\n"
" background-color:#ffffff;\n"
"  border: 2px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  border-radius: 8px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pic_main = QLabel(self.widget)
        self.pic_main.setObjectName(u"pic_main")
        self.pic_main.setMinimumSize(QSize(130, 100))
        self.pic_main.setMaximumSize(QSize(130, 100))
        self.pic_main.setPixmap(QPixmap(u"../picture/logo.png"))
        self.pic_main.setScaledContents(True)
        self.pic_main.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.pic_main)

        self.main_btn = QPushButton(self.widget)
        self.main_btn.setObjectName(u"main_btn")
        font3 = QFont()
        font3.setFamilies([u"B Nazanin"])
        font3.setBold(True)
        self.main_btn.setFont(font3)
        self.main_btn.setStyleSheet(u"QPushButton{\n"
"font-family: \"B Nazanin\";\n"
"background-color:#4CAF50;\n"
"color:white;\n"
"font-size:16px;\n"
"border:none;\n"
"border-radius:5px;\n"
"padding:10 px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #45a049; /* \u0633\u0628\u0632 \u062a\u06cc\u0631\u0647\u200c\u062a\u0631 \u0647\u0646\u06af\u0627\u0645 hover */\n"
"  color: #000;\n"
"  transform: translateY(-2px); /* \u062d\u0631\u06a9\u062a \u062c\u0632\u0626\u06cc \u0628\u0647 \u0628\u0627\u0644\u0627 */\n"
"  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.main_btn)

        self.manager_btn = QPushButton(self.widget)
        self.manager_btn.setObjectName(u"manager_btn")
        self.manager_btn.setFont(font3)
        self.manager_btn.setStyleSheet(u"QPushButton{\n"
"font-family: \"B Nazanin\";\n"
"background-color:#4CAF50;\n"
"color:white;\n"
"font-size:16px;\n"
"border:none;\n"
"border-radius:5px;\n"
"padding:10 px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #45a049; /* \u0633\u0628\u0632 \u062a\u06cc\u0631\u0647\u200c\u062a\u0631 \u0647\u0646\u06af\u0627\u0645 hover */\n"
"  color: #000;\n"
"  transform: translateY(-2px); /* \u062d\u0631\u06a9\u062a \u062c\u0632\u0626\u06cc \u0628\u0647 \u0628\u0627\u0644\u0627 */\n"
"  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.manager_btn)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"font-family: \"B Nazanin\";\n"
"background-color:#4CAF50;\n"
"color:white;\n"
"font-size:16px;\n"
"border:none;\n"
"border-radius:5px;\n"
"padding:10 px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #45a049; /* \u0633\u0628\u0632 \u062a\u06cc\u0631\u0647\u200c\u062a\u0631 \u0647\u0646\u06af\u0627\u0645 hover */\n"
"  color: #000;\n"
"  transform: translateY(-2px); /* \u062d\u0631\u06a9\u062a \u062c\u0632\u0626\u06cc \u0628\u0647 \u0628\u0627\u0644\u0627 */\n"
"  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font3)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"font-family: \"B Nazanin\";\n"
"background-color:#4CAF50;\n"
"color:white;\n"
"font-size:16px;\n"
"border:none;\n"
"border-radius:5px;\n"
"padding:10 px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #45a049; /* \u0633\u0628\u0632 \u062a\u06cc\u0631\u0647\u200c\u062a\u0631 \u0647\u0646\u06af\u0627\u0645 hover */\n"
"  color: #000;\n"
"  transform: translateY(-2px); /* \u062d\u0631\u06a9\u062a \u062c\u0632\u0626\u06cc \u0628\u0647 \u0628\u0627\u0644\u0627 */\n"
"  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font3)
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"font-family: \"B Nazanin\";\n"
"background-color:#4CAF50;\n"
"color:white;\n"
"font-size:16px;\n"
"border:none;\n"
"border-radius:5px;\n"
"padding:10 px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #45a049; /* \u0633\u0628\u0632 \u062a\u06cc\u0631\u0647\u200c\u062a\u0631 \u0647\u0646\u06af\u0627\u0645 hover */\n"
"  color: #000;\n"
"  transform: translateY(-2px); /* \u062d\u0631\u06a9\u062a \u062c\u0632\u0626\u06cc \u0628\u0647 \u0628\u0627\u0644\u0627 */\n"
"  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget_dashboard.setCurrentIndex(1)
        self.mange_tab.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0645\u06cc\u0632\u0627\u0646 \u0627\u0639\u062a\u0628\u0627\u0631 \u0628\u0627\u0642\u06cc\u0645\u0627\u0646\u062f\u0647", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u063a\u0627\u0626\u0628\u06cc\u0646 \u0627\u0645\u0631\u0648\u0632", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u062a\u0627\u062e\u06cc\u0631\u0647\u0627\u06cc \u0627\u0645\u0631\u0648\u0632", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u067e\u06cc\u0627\u0645\u06a9 \u0647\u0627\u06cc \u0627\u0631\u0633\u0627\u0644 \u0634\u062f\u0647 \u0627\u0645\u0631\u0648\u0632", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0647\u0646\u0631\u0633\u062a\u0627\u0646 \u0634\u0647\u06cc\u062f \u0627\u062d\u0645\u062f \u062e\u0648\u0627\u0646\u0633\u0627\u0631\u06cc \u0633\u0627\u0644 \u062a\u062d\u0635\u06cc\u0644\u06cc 1405-1404", None))
        ___qtablewidgetitem = self.class_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"grade", None));
        ___qtablewidgetitem1 = self.class_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"field", None));
        ___qtablewidgetitem2 = self.class_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"class_nam", None));
        self.mange_tab.setTabText(self.mange_tab.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0644\u06cc\u0633\u062a \u06a9\u0644\u0627\u0633\u0647\u0627", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0627\u06cc\u0647 :", None))
        self.Grade_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u062f\u0647\u0645 ", None))
        self.Grade_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u06cc\u0627\u0632\u062f\u0647\u0645", None))
        self.Grade_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u062f\u0648\u0627\u0632\u062f\u0647\u0645", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0634\u062a\u0647:", None))
        self.Field_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0645\u0627\u0634\u06cc\u0646 \u0627\u0628\u0632\u0627\u0631 ", None))
        self.Field_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0633\u0627\u062e\u062a\u0645\u0627\u0646", None))
        self.Field_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0645\u06a9\u0627\u0646\u06cc\u06a9", None))
        self.Field_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0645\u06a9\u0627\u062a\u0631\u0648\u0646\u06cc\u06a9", None))

        self.sub_btn.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a", None))
        self.mange_tab.setTabText(self.mange_tab.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0627\u0641\u0632\u0648\u062f\u0646 \u06a9\u0644\u0627\u0633 \u062c\u062f\u06cc\u062f", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f \u0645\u0644\u06cc:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc :", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u067e\u062f\u0631 :", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0644\u0627\u0633 :", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u062a\u0645\u0627\u0633 :", None))
        self.class_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0631\u06cc\u0627\u0636\u06cc", None))
        self.class_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u062a\u062c\u0631\u0628\u06cc", None))

        self.class_comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"\u0631\u06cc\u0627\u0636\u06cc", None))
        self.student_id_lineEdit.setInputMask("")
        self.submit_student_btn.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0641\u0632\u0648\u062f\u0646", None))
        self.mange_tab.setTabText(self.mange_tab.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0627\u0641\u0632\u0648\u062f\u0646 \u062f\u0627\u0646\u0634 \u0622\u0645\u0648\u0632", None))
        self.mange_tab.setTabText(self.mange_tab.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0648\u06cc\u0631\u0627\u06cc\u0634", None))
        self.pic_main.setText("")
        self.main_btn.setText(QCoreApplication.translate("MainWindow", u"\u0635\u0641\u062d\u0647 \u0627\u0635\u0644\u06cc ", None))
        self.manager_btn.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062f\u06cc\u0631\u06cc\u062a", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u0648\u0636\u0639\u06cc\u062a", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u06af\u0632\u0627\u0631\u0634", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0637\u0644\u0627\u0639 \u0631\u0633\u0627\u0646\u06cc", None))
    # retranslateUi

