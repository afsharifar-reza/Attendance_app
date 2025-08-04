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
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTabWidget, QTableView, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1020, 807)
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
        self.verticalLayout_10 = QVBoxLayout(self.main_page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame = QFrame(self.main_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setPointSize(16)
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

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 0))
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

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 0))
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

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setFamilies([u"B Mitra"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"QLabel{\n"
" background-color:  #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:15 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"}")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.label_7)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
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

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_9 = QLabel(self.frame)
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

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_9)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:15 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"}")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.label_5)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:15 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"}")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.label_2)


        self.verticalLayout_2.addLayout(self.formLayout_2)


        self.verticalLayout_10.addWidget(self.frame)

        self.widget_2 = QWidget(self.main_page)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        font2 = QFont()
        font2.setFamilies([u"B Mitra"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_10)


        self.verticalLayout_10.addWidget(self.widget_2)

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
        self.widget_7.setLayoutDirection(Qt.LeftToRight)
        self.widget_7.setAutoFillBackground(True)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.sub_btn = QPushButton(self.widget_7)
        self.sub_btn.setObjectName(u"sub_btn")

        self.horizontalLayout_7.addWidget(self.sub_btn)

        self.Field_comboBox = QComboBox(self.widget_7)
        self.Field_comboBox.addItem("")
        self.Field_comboBox.addItem("")
        self.Field_comboBox.addItem("")
        self.Field_comboBox.addItem("")
        self.Field_comboBox.setObjectName(u"Field_comboBox")
        self.Field_comboBox.setMinimumSize(QSize(90, 40))
        self.Field_comboBox.setMaximumSize(QSize(90, 16777215))
        self.Field_comboBox.setLayoutDirection(Qt.RightToLeft)
        self.Field_comboBox.setAutoFillBackground(True)
        self.Field_comboBox.setStyleSheet(u"")
        self.Field_comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.Field_comboBox.setFrame(False)

        self.horizontalLayout_7.addWidget(self.Field_comboBox)

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

        self.Grade_comboBox = QComboBox(self.widget_7)
        self.Grade_comboBox.addItem("")
        self.Grade_comboBox.addItem("")
        self.Grade_comboBox.addItem("")
        self.Grade_comboBox.setObjectName(u"Grade_comboBox")
        self.Grade_comboBox.setMinimumSize(QSize(50, 40))
        self.Grade_comboBox.setMaximumSize(QSize(50, 16777215))
        self.Grade_comboBox.setLayoutDirection(Qt.RightToLeft)
        self.Grade_comboBox.setStyleSheet(u"")
        self.Grade_comboBox.setFrame(False)

        self.horizontalLayout_7.addWidget(self.Grade_comboBox)

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
        self.frame_2.setLayoutDirection(Qt.RightToLeft)
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
        self.class_comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.class_comboBox.setLayoutDirection(Qt.RightToLeft)
        self.class_comboBox.setAutoFillBackground(False)
        self.class_comboBox.setStyleSheet(u"QComboBox {\n"
"    font-family: \"B Nazanin\", \"Segoe UI\", Arial;\n"
"    font-size: 13px;\n"
"    color: #495057;\n"
"\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 4px;\n"
"\n"
"    min-width: 200px;\n"
"    min-height: 30px;\n"
"\n"
"    qproperty-layoutDirection: RightToLeft;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    qproperty-layoutDirection: RightToLeft;\n"
"    text-align: right; /* \u0642\u0627\u0628\u0644 \u0686\u0634\u0645\u200c\u067e\u0648\u0634\u06cc\u060c \u062a\u0632\u0626\u06cc\u0646\u06cc */\n"
"}\n"
"\n"
"QComboBox QLineEdit {\n"
"    qproperty-alignment: 'AlignRight';\n"
"    padding-right: 5px;\n"
"}\n"
"")
        self.class_comboBox.setMaxCount(2147483646)
        self.class_comboBox.setInsertPolicy(QComboBox.InsertAtBottom)
        self.class_comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.class_comboBox.setFrame(True)

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
        self.verticalLayout_7 = QVBoxLayout(self.tab_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_18 = QLabel(self.tab_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(80, 0))
        self.label_18.setMaximumSize(QSize(80, 16777215))
        self.label_18.setLayoutDirection(Qt.LeftToRight)
        self.label_18.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_18)

        self.nationalCodeSearchLineEdit = QLineEdit(self.tab_3)
        self.nationalCodeSearchLineEdit.setObjectName(u"nationalCodeSearchLineEdit")
        self.nationalCodeSearchLineEdit.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_13.addWidget(self.nationalCodeSearchLineEdit)

        self.label_19 = QLabel(self.tab_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(70, 0))
        self.label_19.setMaximumSize(QSize(70, 16777215))
        self.label_19.setLayoutDirection(Qt.LeftToRight)
        self.label_19.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_19)

        self.firstNameSearchLineEdit = QLineEdit(self.tab_3)
        self.firstNameSearchLineEdit.setObjectName(u"firstNameSearchLineEdit")
        self.firstNameSearchLineEdit.setStyleSheet(u"QLineEdit {\n"
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
        self.firstNameSearchLineEdit.setMaxLength(32765)

        self.horizontalLayout_13.addWidget(self.firstNameSearchLineEdit)

        self.label_20 = QLabel(self.tab_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(120, 0))
        self.label_20.setMaximumSize(QSize(120, 16777215))
        self.label_20.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_20)

        self.lastNameSearchLineEdit = QLineEdit(self.tab_3)
        self.lastNameSearchLineEdit.setObjectName(u"lastNameSearchLineEdit")
        self.lastNameSearchLineEdit.setStyleSheet(u"QLineEdit {\n"
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
        self.lastNameSearchLineEdit.setMaxLength(32765)

        self.horizontalLayout_13.addWidget(self.lastNameSearchLineEdit)

        self.searchButton = QPushButton(self.tab_3)
        self.searchButton.setObjectName(u"searchButton")

        self.horizontalLayout_13.addWidget(self.searchButton)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.studentTableView = QTableView(self.tab_3)
        self.studentTableView.setObjectName(u"studentTableView")
        self.studentTableView.setStyleSheet(u"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u067e\u0627\u06cc\u0647 \u0628\u0631\u0627\u06cc \u062c\u062f\u0648\u0644 */\n"
"QTableView {\n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0638\u0627\u0647\u0631\u06cc */\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 4px;\n"
"    gridline-color: #f0f0f0;\n"
"    outline: 0;\n"
"    \n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0641\u0648\u0646\u062a */\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    font-size: 12px;\n"
"    color: #333333;\n"
"    \n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0627\u0646\u062a\u062e\u0627\u0628 */\n"
"    selection-background-color: #4a90e2;\n"
"    selection-color: #ffffff;\n"
"    alternate-background-color: #f8f9fa;\n"
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u0647\u062f\u0631\u0647\u0627\u06cc \u0639\u0645\u0648\u062f\u06cc */\n"
"QHeaderView::section:vertical {\n"
"    background-color: #f8f9fa;\n"
"    color: #495057;\n"
"    p"
                        "adding: 8px;\n"
"    border: none;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u0647\u062f\u0631\u0647\u0627\u06cc \u0627\u0641\u0642\u06cc */\n"
"QHeaderView::section:horizontal {\n"
"    background-color: #f8f9fa;\n"
"    color: #495057;\n"
"    padding: 8px;\n"
"    border: none;\n"
"    border-bottom: 1px solid #dee2e6;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* \u0627\u0641\u06a9\u062a hover \u0631\u0648\u06cc \u0647\u062f\u0631\u0647\u0627 */\n"
"QHeaderView::section:hover {\n"
"    background-color: #e9ecef;\n"
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u06af\u0648\u0634\u0647 \u062c\u062f\u0648\u0644 */\n"
"QTableCornerButton::section {\n"
"    background-color: #f8f9fa;\n"
"    border: none;\n"
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u0633\u0637\u0631\u0647\u0627\u06cc \u0645\u062a\u0646\u0627\u0648\u0628 */\n"
"QTableView {\n"
"    alternate-background-color: #f8f9fa;\n"
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u0622\u06cc\u062a"
                        "\u0645\u200c\u0647\u0627 */\n"
"QTableView::item {\n"
"    padding: 6px;\n"
"    border-bottom: 1px solid #f0f0f0;\n"
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u0627\u0633\u06a9\u0631\u0648\u0644 \u0628\u0627\u0631\u0647\u0627 */\n"
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
"    border-radius: 5px;\n"
"}\n"
"\n"
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
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u062d\u0627\u0644\u062a \u0641\u0648\u06a9\u0648\u0633 */\n"
"QTableView::item:focus {\n"
"    border: 1px solid #80bdff;\n"
"    background: rgba(0, 123, 255, 0.1);\n"
"}")
        self.studentTableView.horizontalHeader().setCascadingSectionResizes(False)
        self.studentTableView.horizontalHeader().setDefaultSectionSize(120)
        self.studentTableView.horizontalHeader().setStretchLastSection(True)
        self.studentTableView.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_5.addWidget(self.studentTableView)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.frame_3 = QFrame(self.tab_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setLayoutDirection(Qt.RightToLeft)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(150, 0))
        self.label_21.setMaximumSize(QSize(150, 16777215))
        self.label_21.setLayoutDirection(Qt.LeftToRight)
        self.label_21.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_21)

        self.nationalCodeEditLineEdit = QLineEdit(self.frame_3)
        self.nationalCodeEditLineEdit.setObjectName(u"nationalCodeEditLineEdit")
        self.nationalCodeEditLineEdit.setStyleSheet(u"QLineEdit {\n"
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
        self.nationalCodeEditLineEdit.setMaxLength(32765)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nationalCodeEditLineEdit)

        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(150, 0))
        self.label_22.setMaximumSize(QSize(150, 16777215))
        self.label_22.setLayoutDirection(Qt.LeftToRight)
        self.label_22.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_22)

        self.firstNameEditLineEdit = QLineEdit(self.frame_3)
        self.firstNameEditLineEdit.setObjectName(u"firstNameEditLineEdit")
        self.firstNameEditLineEdit.setStyleSheet(u"QLineEdit {\n"
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

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.firstNameEditLineEdit)

        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(150, 0))
        self.label_23.setMaximumSize(QSize(150, 16777215))
        self.label_23.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_23)

        self.lastNameEditLineEdit = QLineEdit(self.frame_3)
        self.lastNameEditLineEdit.setObjectName(u"lastNameEditLineEdit")
        self.lastNameEditLineEdit.setStyleSheet(u"QLineEdit {\n"
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

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lastNameEditLineEdit)

        self.label_24 = QLabel(self.frame_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(150, 0))
        self.label_24.setMaximumSize(QSize(150, 16777215))
        self.label_24.setLayoutDirection(Qt.LeftToRight)
        self.label_24.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_24)

        self.fatherNameEditLineEdit = QLineEdit(self.frame_3)
        self.fatherNameEditLineEdit.setObjectName(u"fatherNameEditLineEdit")
        self.fatherNameEditLineEdit.setStyleSheet(u"QLineEdit {\n"
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

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.FieldRole, self.fatherNameEditLineEdit)

        self.label_25 = QLabel(self.frame_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(150, 0))
        self.label_25.setMaximumSize(QSize(150, 16777215))
        self.label_25.setLayoutDirection(Qt.LeftToRight)
        self.label_25.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_3.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_25)

        self.class_comboBox_2 = QComboBox(self.frame_3)
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.addItem("")
        self.class_comboBox_2.setObjectName(u"class_comboBox_2")
        self.class_comboBox_2.setMinimumSize(QSize(202, 32))
        self.class_comboBox_2.setMaximumSize(QSize(16777215, 16777215))
        self.class_comboBox_2.setLayoutDirection(Qt.RightToLeft)
        self.class_comboBox_2.setAutoFillBackground(False)
        self.class_comboBox_2.setStyleSheet(u"QComboBox {\n"
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
        self.class_comboBox_2.setMaxCount(2147483646)
        self.class_comboBox_2.setInsertPolicy(QComboBox.InsertAtBottom)
        self.class_comboBox_2.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.class_comboBox_2.setFrame(True)

        self.formLayout_3.setWidget(4, QFormLayout.ItemRole.FieldRole, self.class_comboBox_2)

        self.label_26 = QLabel(self.frame_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(150, 0))
        self.label_26.setMaximumSize(QSize(150, 16777215))
        self.label_26.setLayoutDirection(Qt.LeftToRight)
        self.label_26.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_3.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_26)

        self.phoneNumberEditLineEdit = QLineEdit(self.frame_3)
        self.phoneNumberEditLineEdit.setObjectName(u"phoneNumberEditLineEdit")
        self.phoneNumberEditLineEdit.setStyleSheet(u"QLineEdit {\n"
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

        self.formLayout_3.setWidget(5, QFormLayout.ItemRole.FieldRole, self.phoneNumberEditLineEdit)


        self.verticalLayout_6.addLayout(self.formLayout_3)

        self.widget_9 = QWidget(self.frame_3)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.update_student_btn = QPushButton(self.widget_9)
        self.update_student_btn.setObjectName(u"update_student_btn")

        self.horizontalLayout_14.addWidget(self.update_student_btn)


        self.verticalLayout_6.addWidget(self.widget_9)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.mange_tab.addTab(self.tab_3, "")

        self.horizontalLayout_8.addWidget(self.mange_tab)

        self.stackedWidget_dashboard.addWidget(self.mange_page)
        self.attandance_page = QWidget()
        self.attandance_page.setObjectName(u"attandance_page")
        self.verticalLayout_8 = QVBoxLayout(self.attandance_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.loadButton = QPushButton(self.attandance_page)
        self.loadButton.setObjectName(u"loadButton")

        self.horizontalLayout_15.addWidget(self.loadButton)

        self.dateEdit = QLineEdit(self.attandance_page)
        self.dateEdit.setObjectName(u"dateEdit")

        self.horizontalLayout_15.addWidget(self.dateEdit)

        self.label_28 = QLabel(self.attandance_page)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(100, 0))
        self.label_28.setMaximumSize(QSize(100, 16777215))
        self.label_28.setLayoutDirection(Qt.LeftToRight)
        self.label_28.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_28)

        self.class_comboBox_3 = QComboBox(self.attandance_page)
        self.class_comboBox_3.addItem("")
        self.class_comboBox_3.addItem("")
        self.class_comboBox_3.setObjectName(u"class_comboBox_3")
        self.class_comboBox_3.setMinimumSize(QSize(150, 0))
        self.class_comboBox_3.setMaximumSize(QSize(16777215, 16777215))
        self.class_comboBox_3.setLayoutDirection(Qt.RightToLeft)
        self.class_comboBox_3.setAutoFillBackground(False)
        self.class_comboBox_3.setStyleSheet(u"QComboBox {\n"
"    font-family: \"B Nazanin\", \"Segoe UI\", Arial;\n"
"    font-size: 13px;\n"
"    color: #495057;\n"
"\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 4px;\n"
"\n"
"\n"
"\n"
"    qproperty-layoutDirection: RightToLeft;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    qproperty-layoutDirection: RightToLeft;\n"
"    text-align: right; /* \u0642\u0627\u0628\u0644 \u0686\u0634\u0645\u200c\u067e\u0648\u0634\u06cc\u060c \u062a\u0632\u0626\u06cc\u0646\u06cc */\n"
"}\n"
"\n"
"QComboBox QLineEdit {\n"
"    qproperty-alignment: 'AlignRight';\n"
"    padding-right: 5px;\n"
"}\n"
"")
        self.class_comboBox_3.setMaxCount(2147483646)
        self.class_comboBox_3.setInsertPolicy(QComboBox.InsertAtBottom)
        self.class_comboBox_3.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.class_comboBox_3.setFrame(True)

        self.horizontalLayout_15.addWidget(self.class_comboBox_3)

        self.label_27 = QLabel(self.attandance_page)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(100, 0))
        self.label_27.setMaximumSize(QSize(100, 16777215))
        self.label_27.setLayoutDirection(Qt.LeftToRight)
        self.label_27.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_27)


        self.verticalLayout_8.addLayout(self.horizontalLayout_15)

        self.attendanceTableView = QTableView(self.attandance_page)
        self.attendanceTableView.setObjectName(u"attendanceTableView")
        self.attendanceTableView.setLayoutDirection(Qt.RightToLeft)
        self.attendanceTableView.setStyleSheet(u"QTableView {\n"
"    background-color: #ffffff;\n"
"    gridline-color: #dee2e6;\n"
"    font-family: \"B Nazanin\", \"Segoe UI\", Arial;\n"
"    font-size: 13px;\n"
"    color: #212529;\n"
"    border: 1px solid #ced4da;\n"
"    selection-background-color: #d0ebff;\n"
"    selection-color: #000000;\n"
"    alternate-background-color: #f8f9fa;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f1f3f5;\n"
"    padding: 6px;\n"
"    border: 1px solid #dee2e6;\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"    color: #343a40;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #d0ebff;\n"
"    color: #000;\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.attendanceTableView)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)

        self.cancelButton = QPushButton(self.attandance_page)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_16.addWidget(self.cancelButton)

        self.saveButton = QPushButton(self.attandance_page)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_16.addWidget(self.saveButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_8)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)

        self.stackedWidget_dashboard.addWidget(self.attandance_page)
        self.report_page = QWidget()
        self.report_page.setObjectName(u"report_page")
        self.verticalLayout_9 = QVBoxLayout(self.report_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.report_tab = QTabWidget(self.report_page)
        self.report_tab.setObjectName(u"report_tab")
        self.report_tab.setLayoutDirection(Qt.RightToLeft)
        self.class_report_tab = QWidget()
        self.class_report_tab.setObjectName(u"class_report_tab")
        self.verticalLayout_17 = QVBoxLayout(self.class_report_tab)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_58 = QLabel(self.class_report_tab)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(100, 0))
        self.label_58.setMaximumSize(QSize(100, 16777215))
        self.label_58.setLayoutDirection(Qt.LeftToRight)
        self.label_58.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_58.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.label_58)

        self.class_report_comboBox = QComboBox(self.class_report_tab)
        self.class_report_comboBox.addItem("")
        self.class_report_comboBox.addItem("")
        self.class_report_comboBox.setObjectName(u"class_report_comboBox")
        self.class_report_comboBox.setMinimumSize(QSize(150, 30))
        self.class_report_comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.class_report_comboBox.setLayoutDirection(Qt.RightToLeft)
        self.class_report_comboBox.setAutoFillBackground(False)
        self.class_report_comboBox.setStyleSheet(u"QComboBox {\n"
"    font-family: \"B Nazanin\", \"Segoe UI\", Arial;\n"
"    font-size: 13px;\n"
"    color: #495057;\n"
"\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 4px;\n"
"\n"
"\n"
"\n"
"    qproperty-layoutDirection: RightToLeft;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    qproperty-layoutDirection: RightToLeft;\n"
"    text-align: right; /* \u0642\u0627\u0628\u0644 \u0686\u0634\u0645\u200c\u067e\u0648\u0634\u06cc\u060c \u062a\u0632\u0626\u06cc\u0646\u06cc */\n"
"}\n"
"\n"
"QComboBox QLineEdit {\n"
"    qproperty-alignment: 'AlignRight';\n"
"    padding-right: 5px;\n"
"}\n"
"")
        self.class_report_comboBox.setMaxCount(2147483646)
        self.class_report_comboBox.setInsertPolicy(QComboBox.InsertAtBottom)
        self.class_report_comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.class_report_comboBox.setFrame(True)

        self.horizontalLayout_32.addWidget(self.class_report_comboBox)

        self.label_57 = QLabel(self.class_report_tab)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(100, 0))
        self.label_57.setMaximumSize(QSize(100, 16777215))
        self.label_57.setLayoutDirection(Qt.LeftToRight)
        self.label_57.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_57.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.label_57)

        self.start_class_dateEdit = QLineEdit(self.class_report_tab)
        self.start_class_dateEdit.setObjectName(u"start_class_dateEdit")
        self.start_class_dateEdit.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_32.addWidget(self.start_class_dateEdit)

        self.label_59 = QLabel(self.class_report_tab)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(100, 0))
        self.label_59.setMaximumSize(QSize(100, 16777215))
        self.label_59.setLayoutDirection(Qt.LeftToRight)
        self.label_59.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_59.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.label_59)

        self.end_class_dateEdit = QLineEdit(self.class_report_tab)
        self.end_class_dateEdit.setObjectName(u"end_class_dateEdit")
        self.end_class_dateEdit.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_32.addWidget(self.end_class_dateEdit)

        self.class_report_btn = QPushButton(self.class_report_tab)
        self.class_report_btn.setObjectName(u"class_report_btn")

        self.horizontalLayout_32.addWidget(self.class_report_btn)


        self.verticalLayout_17.addLayout(self.horizontalLayout_32)

        self.class_report_table = QTableView(self.class_report_tab)
        self.class_report_table.setObjectName(u"class_report_table")
        self.class_report_table.setStyleSheet(u"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u067e\u0627\u06cc\u0647 \u0628\u0631\u0627\u06cc \u062c\u062f\u0648\u0644 */\n"
"QTableView {\n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0638\u0627\u0647\u0631\u06cc */\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 4px;\n"
"    gridline-color: #f0f0f0;\n"
"    outline: 0;\n"
"    \n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0641\u0648\u0646\u062a */\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    font-size: 12px;\n"
"    color: #333333;\n"
"    \n"
"    /* \u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0627\u0646\u062a\u062e\u0627\u0628 */\n"
"    selection-background-color: #4a90e2;\n"
"    selection-color: #ffffff;\n"
"    alternate-background-color: #f8f9fa;\n"
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u0647\u062f\u0631\u0647\u0627\u06cc \u0639\u0645\u0648\u062f\u06cc */\n"
"QHeaderView::section:vertical {\n"
"    background-color: #f8f9fa;\n"
"    color: #495057;\n"
"    p"
                        "adding: 8px;\n"
"    border: none;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u0647\u062f\u0631\u0647\u0627\u06cc \u0627\u0641\u0642\u06cc */\n"
"QHeaderView::section:horizontal {\n"
"    background-color: #f8f9fa;\n"
"    color: #495057;\n"
"    padding: 8px;\n"
"    border: none;\n"
"    border-bottom: 1px solid #dee2e6;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* \u0627\u0641\u06a9\u062a hover \u0631\u0648\u06cc \u0647\u062f\u0631\u0647\u0627 */\n"
"QHeaderView::section:hover {\n"
"    background-color: #e9ecef;\n"
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u06af\u0648\u0634\u0647 \u062c\u062f\u0648\u0644 */\n"
"QTableCornerButton::section {\n"
"    background-color: #f8f9fa;\n"
"    border: none;\n"
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u0633\u0637\u0631\u0647\u0627\u06cc \u0645\u062a\u0646\u0627\u0648\u0628 */\n"
"QTableView {\n"
"    alternate-background-color: #f8f9fa;\n"
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u0622\u06cc\u062a"
                        "\u0645\u200c\u0647\u0627 */\n"
"QTableView::item {\n"
"    padding: 6px;\n"
"    border-bottom: 1px solid #f0f0f0;\n"
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u0627\u0633\u06a9\u0631\u0648\u0644 \u0628\u0627\u0631\u0647\u0627 */\n"
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
"    border-radius: 5px;\n"
"}\n"
"\n"
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
"}\n"
"\n"
"/* \u0627\u0633\u062a\u0627\u06cc\u0644 \u062d\u0627\u0644\u062a \u0641\u0648\u06a9\u0648\u0633 */\n"
"QTableView::item:focus {\n"
"    border: 1px solid #80bdff;\n"
"    background: rgba(0, 123, 255, 0.1);\n"
"}")

        self.verticalLayout_17.addWidget(self.class_report_table)

        self.report_tab.addTab(self.class_report_tab, "")
        self.student_report_tab = QWidget()
        self.student_report_tab.setObjectName(u"student_report_tab")
        self.verticalLayout_11 = QVBoxLayout(self.student_report_tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_32 = QLabel(self.student_report_tab)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(80, 0))
        self.label_32.setMaximumSize(QSize(80, 16777215))
        self.label_32.setLayoutDirection(Qt.LeftToRight)
        self.label_32.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_32.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_32)

        self.stu_report_nationalCode_lineEdit = QLineEdit(self.student_report_tab)
        self.stu_report_nationalCode_lineEdit.setObjectName(u"stu_report_nationalCode_lineEdit")
        self.stu_report_nationalCode_lineEdit.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_18.addWidget(self.stu_report_nationalCode_lineEdit)

        self.label_33 = QLabel(self.student_report_tab)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(70, 0))
        self.label_33.setMaximumSize(QSize(70, 16777215))
        self.label_33.setLayoutDirection(Qt.LeftToRight)
        self.label_33.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_33.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_33)

        self.stu_report_firstName_lineEdit = QLineEdit(self.student_report_tab)
        self.stu_report_firstName_lineEdit.setObjectName(u"stu_report_firstName_lineEdit")
        self.stu_report_firstName_lineEdit.setStyleSheet(u"QLineEdit {\n"
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
        self.stu_report_firstName_lineEdit.setMaxLength(32765)

        self.horizontalLayout_18.addWidget(self.stu_report_firstName_lineEdit)

        self.label_34 = QLabel(self.student_report_tab)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(120, 0))
        self.label_34.setMaximumSize(QSize(120, 16777215))
        self.label_34.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_34.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_34)

        self.stu_report_lastName_lineEdit = QLineEdit(self.student_report_tab)
        self.stu_report_lastName_lineEdit.setObjectName(u"stu_report_lastName_lineEdit")
        self.stu_report_lastName_lineEdit.setStyleSheet(u"QLineEdit {\n"
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
        self.stu_report_lastName_lineEdit.setMaxLength(32765)

        self.horizontalLayout_18.addWidget(self.stu_report_lastName_lineEdit)

        self.stu_report_search_btn = QPushButton(self.student_report_tab)
        self.stu_report_search_btn.setObjectName(u"stu_report_search_btn")

        self.horizontalLayout_18.addWidget(self.stu_report_search_btn)


        self.verticalLayout_11.addLayout(self.horizontalLayout_18)

        self.search_table_view = QTableView(self.student_report_tab)
        self.search_table_view.setObjectName(u"search_table_view")
        self.search_table_view.setMaximumSize(QSize(16777215, 200))
        self.search_table_view.setStyleSheet(u"QTableView {\n"
"    background-color: #ffffff;\n"
"    gridline-color: #dee2e6;\n"
"    font-family: \"B Nazanin\", \"Segoe UI\", Arial;\n"
"    font-size: 13px;\n"
"    color: #212529;\n"
"    border: 1px solid #ced4da;\n"
"    selection-background-color: #d0ebff;\n"
"    selection-color: #000000;\n"
"    alternate-background-color: #f8f9fa;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f1f3f5;\n"
"    padding: 6px;\n"
"    border: 1px solid #dee2e6;\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"    color: #343a40;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #d0ebff;\n"
"    color: #000;\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.search_table_view)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.stu_detail_nationalCode_lineEdit = QLineEdit(self.student_report_tab)
        self.stu_detail_nationalCode_lineEdit.setObjectName(u"stu_detail_nationalCode_lineEdit")
        self.stu_detail_nationalCode_lineEdit.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_19.addWidget(self.stu_detail_nationalCode_lineEdit)

        self.stu_detail_firstName_lineEdit = QLineEdit(self.student_report_tab)
        self.stu_detail_firstName_lineEdit.setObjectName(u"stu_detail_firstName_lineEdit")
        self.stu_detail_firstName_lineEdit.setStyleSheet(u"QLineEdit {\n"
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
        self.stu_detail_firstName_lineEdit.setMaxLength(32765)

        self.horizontalLayout_19.addWidget(self.stu_detail_firstName_lineEdit)

        self.stu_detail_lastName_lineEdit = QLineEdit(self.student_report_tab)
        self.stu_detail_lastName_lineEdit.setObjectName(u"stu_detail_lastName_lineEdit")
        self.stu_detail_lastName_lineEdit.setStyleSheet(u"QLineEdit {\n"
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
        self.stu_detail_lastName_lineEdit.setMaxLength(32765)

        self.horizontalLayout_19.addWidget(self.stu_detail_lastName_lineEdit)

        self.stu_detail_className_lineEdit = QLineEdit(self.student_report_tab)
        self.stu_detail_className_lineEdit.setObjectName(u"stu_detail_className_lineEdit")
        self.stu_detail_className_lineEdit.setStyleSheet(u"QLineEdit {\n"
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
        self.stu_detail_className_lineEdit.setMaxLength(32765)

        self.horizontalLayout_19.addWidget(self.stu_detail_className_lineEdit)


        self.verticalLayout_11.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_61 = QLabel(self.student_report_tab)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(100, 0))
        self.label_61.setMaximumSize(QSize(100, 16777215))
        self.label_61.setLayoutDirection(Qt.LeftToRight)
        self.label_61.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_61.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_33.addWidget(self.label_61)

        self.stu_report_from_dateEdit = QLineEdit(self.student_report_tab)
        self.stu_report_from_dateEdit.setObjectName(u"stu_report_from_dateEdit")
        self.stu_report_from_dateEdit.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_33.addWidget(self.stu_report_from_dateEdit)

        self.label_62 = QLabel(self.student_report_tab)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(100, 0))
        self.label_62.setMaximumSize(QSize(100, 16777215))
        self.label_62.setLayoutDirection(Qt.LeftToRight)
        self.label_62.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_62.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_33.addWidget(self.label_62)

        self.stu_report_to_dateEdit = QLineEdit(self.student_report_tab)
        self.stu_report_to_dateEdit.setObjectName(u"stu_report_to_dateEdit")
        self.stu_report_to_dateEdit.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_33.addWidget(self.stu_report_to_dateEdit)

        self.stu_report_status_comboBox = QComboBox(self.student_report_tab)
        self.stu_report_status_comboBox.addItem("")
        self.stu_report_status_comboBox.addItem("")
        self.stu_report_status_comboBox.addItem("")
        self.stu_report_status_comboBox.addItem("")
        self.stu_report_status_comboBox.setObjectName(u"stu_report_status_comboBox")

        self.horizontalLayout_33.addWidget(self.stu_report_status_comboBox)

        self.stu_report_show_report_btn = QPushButton(self.student_report_tab)
        self.stu_report_show_report_btn.setObjectName(u"stu_report_show_report_btn")

        self.horizontalLayout_33.addWidget(self.stu_report_show_report_btn)


        self.verticalLayout_11.addLayout(self.horizontalLayout_33)

        self.stu_report_tableView = QTableView(self.student_report_tab)
        self.stu_report_tableView.setObjectName(u"stu_report_tableView")
        self.stu_report_tableView.setStyleSheet(u"QTableView {\n"
"    background-color: #ffffff;\n"
"    gridline-color: #dee2e6;\n"
"    font-family: \"B Nazanin\", \"Segoe UI\", Arial;\n"
"    font-size: 13px;\n"
"    color: #212529;\n"
"    border: 1px solid #ced4da;\n"
"    selection-background-color: #d0ebff;\n"
"    selection-color: #000000;\n"
"    alternate-background-color: #f8f9fa;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f1f3f5;\n"
"    padding: 6px;\n"
"    border: 1px solid #dee2e6;\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"    color: #343a40;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #d0ebff;\n"
"    color: #000;\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.stu_report_tableView)

        self.report_tab.addTab(self.student_report_tab, "")

        self.verticalLayout_9.addWidget(self.report_tab)

        self.stackedWidget_dashboard.addWidget(self.report_page)
        self.sms_page = QWidget()
        self.sms_page.setObjectName(u"sms_page")
        self.verticalLayout_12 = QVBoxLayout(self.sms_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.sms_tab = QTabWidget(self.sms_page)
        self.sms_tab.setObjectName(u"sms_tab")
        self.sms_tab.setLayoutDirection(Qt.RightToLeft)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_13 = QVBoxLayout(self.tab_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.sms_class_comboBox = QComboBox(self.tab_5)
        self.sms_class_comboBox.addItem("")
        self.sms_class_comboBox.setObjectName(u"sms_class_comboBox")
        self.sms_class_comboBox.setMinimumSize(QSize(150, 40))
        self.sms_class_comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.sms_class_comboBox.setLayoutDirection(Qt.RightToLeft)
        self.sms_class_comboBox.setAutoFillBackground(False)
        self.sms_class_comboBox.setStyleSheet(u"QComboBox {\n"
"    font-family: \"B Nazanin\", \"Segoe UI\", Arial;\n"
"    font-size: 13px;\n"
"    color: #495057;\n"
"\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 4px;\n"
"\n"
"\n"
"\n"
"    qproperty-layoutDirection: RightToLeft;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    qproperty-layoutDirection: RightToLeft;\n"
"    text-align: right; /* \u0642\u0627\u0628\u0644 \u0686\u0634\u0645\u200c\u067e\u0648\u0634\u06cc\u060c \u062a\u0632\u0626\u06cc\u0646\u06cc */\n"
"}\n"
"\n"
"QComboBox QLineEdit {\n"
"    qproperty-alignment: 'AlignRight';\n"
"    padding-right: 5px;\n"
"}\n"
"")
        self.sms_class_comboBox.setMaxCount(2147483646)
        self.sms_class_comboBox.setInsertPolicy(QComboBox.InsertAtBottom)
        self.sms_class_comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.sms_class_comboBox.setFrame(True)

        self.gridLayout.addWidget(self.sms_class_comboBox, 0, 3, 1, 1)

        self.stu_report_nationalCode_lineEdit_2 = QLineEdit(self.tab_5)
        self.stu_report_nationalCode_lineEdit_2.setObjectName(u"stu_report_nationalCode_lineEdit_2")
        self.stu_report_nationalCode_lineEdit_2.setMinimumSize(QSize(0, 40))
        self.stu_report_nationalCode_lineEdit_2.setStyleSheet(u"QLineEdit {\n"
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

        self.gridLayout.addWidget(self.stu_report_nationalCode_lineEdit_2, 0, 1, 1, 1)

        self.stu_report_lastName_lineEdit_2 = QLineEdit(self.tab_5)
        self.stu_report_lastName_lineEdit_2.setObjectName(u"stu_report_lastName_lineEdit_2")
        self.stu_report_lastName_lineEdit_2.setMinimumSize(QSize(0, 40))
        self.stu_report_lastName_lineEdit_2.setStyleSheet(u"QLineEdit {\n"
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
        self.stu_report_lastName_lineEdit_2.setMaxLength(32765)

        self.gridLayout.addWidget(self.stu_report_lastName_lineEdit_2, 1, 3, 1, 1)

        self.stu_report_firstName_lineEdit_2 = QLineEdit(self.tab_5)
        self.stu_report_firstName_lineEdit_2.setObjectName(u"stu_report_firstName_lineEdit_2")
        self.stu_report_firstName_lineEdit_2.setMinimumSize(QSize(0, 40))
        self.stu_report_firstName_lineEdit_2.setStyleSheet(u"QLineEdit {\n"
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
        self.stu_report_firstName_lineEdit_2.setMaxLength(32765)

        self.gridLayout.addWidget(self.stu_report_firstName_lineEdit_2, 1, 1, 1, 1)

        self.label_37 = QLabel(self.tab_5)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(100, 0))
        self.label_37.setMaximumSize(QSize(100, 16777215))
        self.label_37.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_37.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_37, 1, 2, 1, 1)

        self.label_29 = QLabel(self.tab_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(100, 0))
        self.label_29.setMaximumSize(QSize(100, 16777215))
        self.label_29.setLayoutDirection(Qt.LeftToRight)
        self.label_29.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_29, 0, 4, 1, 1)

        self.label_36 = QLabel(self.tab_5)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(80, 0))
        self.label_36.setMaximumSize(QSize(80, 16777215))
        self.label_36.setLayoutDirection(Qt.LeftToRight)
        self.label_36.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_36.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_36, 1, 0, 1, 1)

        self.label_35 = QLabel(self.tab_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(80, 0))
        self.label_35.setMaximumSize(QSize(80, 16777215))
        self.label_35.setLayoutDirection(Qt.LeftToRight)
        self.label_35.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_35.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_35, 0, 0, 1, 1)

        self.dateEdit_2 = QLineEdit(self.tab_5)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.dateEdit_2, 0, 5, 1, 1)

        self.label_60 = QLabel(self.tab_5)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(100, 0))
        self.label_60.setMaximumSize(QSize(100, 16777215))
        self.label_60.setLayoutDirection(Qt.LeftToRight)
        self.label_60.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_60.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_60, 0, 2, 1, 1)

        self.pushButton = QPushButton(self.tab_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.pushButton, 1, 5, 1, 1)


        self.verticalLayout_13.addLayout(self.gridLayout)

        self.tableView = QTableView(self.tab_5)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_13.addWidget(self.tableView)

        self.widget_3 = QWidget(self.tab_5)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_13.addWidget(self.widget_3)

        self.sms_tab.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_14 = QVBoxLayout(self.tab_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.class_report_comboBox_3 = QComboBox(self.tab_6)
        self.class_report_comboBox_3.addItem("")
        self.class_report_comboBox_3.setObjectName(u"class_report_comboBox_3")
        self.class_report_comboBox_3.setMinimumSize(QSize(150, 40))
        self.class_report_comboBox_3.setMaximumSize(QSize(16777215, 16777215))
        self.class_report_comboBox_3.setLayoutDirection(Qt.RightToLeft)
        self.class_report_comboBox_3.setAutoFillBackground(False)
        self.class_report_comboBox_3.setStyleSheet(u"QComboBox {\n"
"    font-family: \"B Nazanin\", \"Segoe UI\", Arial;\n"
"    font-size: 13px;\n"
"    color: #495057;\n"
"\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 4px;\n"
"\n"
"\n"
"\n"
"    qproperty-layoutDirection: RightToLeft;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    qproperty-layoutDirection: RightToLeft;\n"
"    text-align: right; /* \u0642\u0627\u0628\u0644 \u0686\u0634\u0645\u200c\u067e\u0648\u0634\u06cc\u060c \u062a\u0632\u0626\u06cc\u0646\u06cc */\n"
"}\n"
"\n"
"QComboBox QLineEdit {\n"
"    qproperty-alignment: 'AlignRight';\n"
"    padding-right: 5px;\n"
"}\n"
"")
        self.class_report_comboBox_3.setMaxCount(2147483646)
        self.class_report_comboBox_3.setInsertPolicy(QComboBox.InsertAtBottom)
        self.class_report_comboBox_3.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.class_report_comboBox_3.setFrame(True)

        self.gridLayout_2.addWidget(self.class_report_comboBox_3, 0, 3, 1, 1)

        self.stu_report_nationalCode_lineEdit_3 = QLineEdit(self.tab_6)
        self.stu_report_nationalCode_lineEdit_3.setObjectName(u"stu_report_nationalCode_lineEdit_3")
        self.stu_report_nationalCode_lineEdit_3.setMinimumSize(QSize(0, 40))
        self.stu_report_nationalCode_lineEdit_3.setStyleSheet(u"QLineEdit {\n"
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

        self.gridLayout_2.addWidget(self.stu_report_nationalCode_lineEdit_3, 0, 1, 1, 1)

        self.stu_report_lastName_lineEdit_3 = QLineEdit(self.tab_6)
        self.stu_report_lastName_lineEdit_3.setObjectName(u"stu_report_lastName_lineEdit_3")
        self.stu_report_lastName_lineEdit_3.setMinimumSize(QSize(0, 40))
        self.stu_report_lastName_lineEdit_3.setStyleSheet(u"QLineEdit {\n"
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
        self.stu_report_lastName_lineEdit_3.setMaxLength(32765)

        self.gridLayout_2.addWidget(self.stu_report_lastName_lineEdit_3, 1, 3, 1, 1)

        self.stu_report_firstName_lineEdit_3 = QLineEdit(self.tab_6)
        self.stu_report_firstName_lineEdit_3.setObjectName(u"stu_report_firstName_lineEdit_3")
        self.stu_report_firstName_lineEdit_3.setMinimumSize(QSize(0, 40))
        self.stu_report_firstName_lineEdit_3.setStyleSheet(u"QLineEdit {\n"
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
        self.stu_report_firstName_lineEdit_3.setMaxLength(32765)

        self.gridLayout_2.addWidget(self.stu_report_firstName_lineEdit_3, 1, 1, 1, 1)

        self.label_38 = QLabel(self.tab_6)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(100, 0))
        self.label_38.setMaximumSize(QSize(100, 16777215))
        self.label_38.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_38.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_38, 1, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.tab_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 5, 1, 1)

        self.label_30 = QLabel(self.tab_6)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(100, 0))
        self.label_30.setMaximumSize(QSize(100, 16777215))
        self.label_30.setLayoutDirection(Qt.LeftToRight)
        self.label_30.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_30, 0, 4, 1, 1)

        self.label_39 = QLabel(self.tab_6)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(80, 0))
        self.label_39.setMaximumSize(QSize(80, 16777215))
        self.label_39.setLayoutDirection(Qt.LeftToRight)
        self.label_39.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_39.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_39, 1, 0, 1, 1)

        self.dateEdit_3 = QLineEdit(self.tab_6)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.dateEdit_3, 0, 5, 1, 1)

        self.label_63 = QLabel(self.tab_6)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(100, 0))
        self.label_63.setMaximumSize(QSize(100, 16777215))
        self.label_63.setLayoutDirection(Qt.LeftToRight)
        self.label_63.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_63.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_63, 0, 2, 1, 1)

        self.label_40 = QLabel(self.tab_6)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(80, 0))
        self.label_40.setMaximumSize(QSize(80, 16777215))
        self.label_40.setLayoutDirection(Qt.LeftToRight)
        self.label_40.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_40.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_40, 0, 0, 1, 1)


        self.verticalLayout_14.addLayout(self.gridLayout_2)

        self.tableView_2 = QTableView(self.tab_6)
        self.tableView_2.setObjectName(u"tableView_2")

        self.verticalLayout_14.addWidget(self.tableView_2)

        self.widget_4 = QWidget(self.tab_6)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.pushButton_6 = QPushButton(self.widget_4)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)


        self.verticalLayout_14.addWidget(self.widget_4)

        self.sms_tab.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_15 = QVBoxLayout(self.tab_7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.class_report_comboBox_4 = QComboBox(self.tab_7)
        self.class_report_comboBox_4.addItem("")
        self.class_report_comboBox_4.setObjectName(u"class_report_comboBox_4")
        self.class_report_comboBox_4.setMinimumSize(QSize(150, 40))
        self.class_report_comboBox_4.setMaximumSize(QSize(16777215, 16777215))
        self.class_report_comboBox_4.setLayoutDirection(Qt.RightToLeft)
        self.class_report_comboBox_4.setAutoFillBackground(False)
        self.class_report_comboBox_4.setStyleSheet(u"QComboBox {\n"
"    font-family: \"B Nazanin\", \"Segoe UI\", Arial;\n"
"    font-size: 13px;\n"
"    color: #495057;\n"
"\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 4px;\n"
"\n"
"\n"
"\n"
"    qproperty-layoutDirection: RightToLeft;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    qproperty-layoutDirection: RightToLeft;\n"
"    text-align: right; /* \u0642\u0627\u0628\u0644 \u0686\u0634\u0645\u200c\u067e\u0648\u0634\u06cc\u060c \u062a\u0632\u0626\u06cc\u0646\u06cc */\n"
"}\n"
"\n"
"QComboBox QLineEdit {\n"
"    qproperty-alignment: 'AlignRight';\n"
"    padding-right: 5px;\n"
"}\n"
"")
        self.class_report_comboBox_4.setMaxCount(2147483646)
        self.class_report_comboBox_4.setInsertPolicy(QComboBox.InsertAtBottom)
        self.class_report_comboBox_4.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.class_report_comboBox_4.setFrame(True)

        self.gridLayout_3.addWidget(self.class_report_comboBox_4, 0, 3, 1, 1)

        self.stu_report_nationalCode_lineEdit_4 = QLineEdit(self.tab_7)
        self.stu_report_nationalCode_lineEdit_4.setObjectName(u"stu_report_nationalCode_lineEdit_4")
        self.stu_report_nationalCode_lineEdit_4.setMinimumSize(QSize(0, 40))
        self.stu_report_nationalCode_lineEdit_4.setStyleSheet(u"QLineEdit {\n"
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

        self.gridLayout_3.addWidget(self.stu_report_nationalCode_lineEdit_4, 0, 1, 1, 1)

        self.stu_report_lastName_lineEdit_4 = QLineEdit(self.tab_7)
        self.stu_report_lastName_lineEdit_4.setObjectName(u"stu_report_lastName_lineEdit_4")
        self.stu_report_lastName_lineEdit_4.setMinimumSize(QSize(0, 40))
        self.stu_report_lastName_lineEdit_4.setStyleSheet(u"QLineEdit {\n"
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
        self.stu_report_lastName_lineEdit_4.setMaxLength(32765)

        self.gridLayout_3.addWidget(self.stu_report_lastName_lineEdit_4, 1, 3, 1, 1)

        self.stu_report_firstName_lineEdit_4 = QLineEdit(self.tab_7)
        self.stu_report_firstName_lineEdit_4.setObjectName(u"stu_report_firstName_lineEdit_4")
        self.stu_report_firstName_lineEdit_4.setMinimumSize(QSize(0, 40))
        self.stu_report_firstName_lineEdit_4.setStyleSheet(u"QLineEdit {\n"
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
        self.stu_report_firstName_lineEdit_4.setMaxLength(32765)

        self.gridLayout_3.addWidget(self.stu_report_firstName_lineEdit_4, 1, 1, 1, 1)

        self.label_41 = QLabel(self.tab_7)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(100, 0))
        self.label_41.setMaximumSize(QSize(100, 16777215))
        self.label_41.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_41, 1, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.tab_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.pushButton_4, 1, 5, 1, 1)

        self.label_31 = QLabel(self.tab_7)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(100, 0))
        self.label_31.setMaximumSize(QSize(100, 16777215))
        self.label_31.setLayoutDirection(Qt.LeftToRight)
        self.label_31.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_31.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_31, 0, 4, 1, 1)

        self.label_42 = QLabel(self.tab_7)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(80, 0))
        self.label_42.setMaximumSize(QSize(80, 16777215))
        self.label_42.setLayoutDirection(Qt.LeftToRight)
        self.label_42.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_42.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_42, 1, 0, 1, 1)

        self.dateEdit_4 = QLineEdit(self.tab_7)
        self.dateEdit_4.setObjectName(u"dateEdit_4")
        self.dateEdit_4.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.dateEdit_4, 0, 5, 1, 1)

        self.label_64 = QLabel(self.tab_7)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(100, 0))
        self.label_64.setMaximumSize(QSize(100, 16777215))
        self.label_64.setLayoutDirection(Qt.LeftToRight)
        self.label_64.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_64.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_64, 0, 2, 1, 1)

        self.label_43 = QLabel(self.tab_7)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(80, 0))
        self.label_43.setMaximumSize(QSize(80, 16777215))
        self.label_43.setLayoutDirection(Qt.LeftToRight)
        self.label_43.setStyleSheet(u"QLabel{\n"
" background-color: #ffffff;\n"
"  border: 1px solid #795548; /* \u06a9\u0627\u062f\u0631 \u062f\u0648\u0631 \u0641\u0631\u06cc\u0645 (\u0636\u062e\u0627\u0645\u062a 2px \u0648 \u0631\u0646\u06af \u0642\u0647\u0648\u0647\u200c\u0627\u06cc) */\n"
"  padding:5 px;\n"
"  border-radius: 10px; /* \u0644\u0628\u0647\u200c\u0647\u0627\u06cc \u06af\u0631\u062f */\n"
"  text-align:center;\n"
"  font-family: \"B Nazanin\";\n"
"  font-size: 15px;\n"
"  font-weight: bold;\n"
"}")
        self.label_43.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_43, 0, 0, 1, 1)


        self.verticalLayout_15.addLayout(self.gridLayout_3)

        self.tableView_3 = QTableView(self.tab_7)
        self.tableView_3.setObjectName(u"tableView_3")

        self.verticalLayout_15.addWidget(self.tableView_3)

        self.widget_5 = QWidget(self.tab_7)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)

        self.pushButton_7 = QPushButton(self.widget_5)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_4.addWidget(self.pushButton_7)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_12)


        self.verticalLayout_15.addWidget(self.widget_5)

        self.sms_tab.addTab(self.tab_7, "")

        self.verticalLayout_12.addWidget(self.sms_tab)

        self.stackedWidget_dashboard.addWidget(self.sms_page)

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

        self.attandance_btn = QPushButton(self.widget)
        self.attandance_btn.setObjectName(u"attandance_btn")
        self.attandance_btn.setFont(font3)
        self.attandance_btn.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout.addWidget(self.attandance_btn)

        self.report_btn = QPushButton(self.widget)
        self.report_btn.setObjectName(u"report_btn")
        self.report_btn.setFont(font3)
        self.report_btn.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout.addWidget(self.report_btn)

        self.sms_btn = QPushButton(self.widget)
        self.sms_btn.setObjectName(u"sms_btn")
        self.sms_btn.setFont(font3)
        self.sms_btn.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout.addWidget(self.sms_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1020, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget_dashboard.setCurrentIndex(4)
        self.mange_tab.setCurrentIndex(3)
        self.report_tab.setCurrentIndex(1)
        self.sms_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u062a\u0627\u062e\u06cc\u0631\u0647\u0627\u06cc \u0627\u0645\u0631\u0648\u0632", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u067e\u06cc\u0627\u0645\u06a9 \u0647\u0627\u06cc \u0627\u0631\u0633\u0627\u0644 \u0634\u062f\u0647 \u0627\u0645\u0631\u0648\u0632", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0639\u062f\u0627\u062f \u063a\u0627\u0626\u0628\u06cc\u0646 \u0627\u0645\u0631\u0648\u0632", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0645\u06cc\u0632\u0627\u0646 \u0627\u0639\u062a\u0628\u0627\u0631 \u0628\u0627\u0642\u06cc\u0645\u0627\u0646\u062f\u0647", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0647\u0646\u0631\u0633\u062a\u0627\u0646 \u0634\u0647\u06cc\u062f \u0627\u062d\u0645\u062f \u062e\u0648\u0627\u0646\u0633\u0627\u0631\u06cc \u0633\u0627\u0644 \u062a\u062d\u0635\u06cc\u0644\u06cc 1405-1404", None))
        ___qtablewidgetitem = self.class_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"grade", None));
        ___qtablewidgetitem1 = self.class_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"field", None));
        ___qtablewidgetitem2 = self.class_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"class_nam", None));
        self.mange_tab.setTabText(self.mange_tab.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0644\u06cc\u0633\u062a \u06a9\u0644\u0627\u0633\u0647\u0627", None))
        self.sub_btn.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a", None))
        self.Field_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0645\u0627\u0634\u06cc\u0646 \u0627\u0628\u0632\u0627\u0631 ", None))
        self.Field_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0633\u0627\u062e\u062a\u0645\u0627\u0646", None))
        self.Field_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0645\u06a9\u0627\u0646\u06cc\u06a9", None))
        self.Field_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0645\u06a9\u0627\u062a\u0631\u0648\u0646\u06cc\u06a9", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0634\u062a\u0647:", None))
        self.Grade_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u062f\u0647\u0645 ", None))
        self.Grade_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u06cc\u0627\u0632\u062f\u0647\u0645", None))
        self.Grade_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u062f\u0648\u0627\u0632\u062f\u0647\u0645", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0627\u06cc\u0647 :", None))
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
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f \u0645\u0644\u06cc:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645:", None))
        self.firstNameSearchLineEdit.setInputMask("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc :", None))
        self.lastNameSearchLineEdit.setInputMask("")
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a\u062c\u0648", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f \u0645\u0644\u06cc:", None))
        self.nationalCodeEditLineEdit.setInputMask("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc :", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u067e\u062f\u0631 :", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0644\u0627\u0633 :", None))
        self.class_comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0631\u06cc\u0627\u0636\u06cc", None))
        self.class_comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u062a\u062c\u0631\u0628\u06cc", None))

        self.class_comboBox_2.setCurrentText(QCoreApplication.translate("MainWindow", u"\u0631\u06cc\u0627\u0636\u06cc", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0634\u0645\u0627\u0631\u0647 \u062a\u0645\u0627\u0633 :", None))
        self.update_student_btn.setText(QCoreApplication.translate("MainWindow", u"\u0648\u06cc\u0631\u0627\u06cc\u0634", None))
        self.mange_tab.setTabText(self.mange_tab.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0648\u06cc\u0631\u0627\u06cc\u0634", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0631\u06af\u0630\u0627\u0631\u06cc \u0644\u06cc\u0633\u062a", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e:", None))
        self.class_comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0631\u06cc\u0627\u0636\u06cc", None))
        self.class_comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"\u062a\u062c\u0631\u0628\u06cc", None))

        self.class_comboBox_3.setCurrentText(QCoreApplication.translate("MainWindow", u"\u0631\u06cc\u0627\u0636\u06cc", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0644\u0627\u0633 :", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"\u0644\u063a\u0648", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"\u0630\u062e\u06cc\u0631\u0647", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0644\u0627\u0633 :", None))
        self.class_report_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0631\u06cc\u0627\u0636\u06cc", None))
        self.class_report_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u062a\u062c\u0631\u0628\u06cc", None))

        self.class_report_comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"\u0631\u06cc\u0627\u0636\u06cc", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0632 \u062a\u0627\u0631\u06cc\u062e:", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627 \u062a\u0627\u0631\u06cc\u062e:", None))
        self.class_report_btn.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0639\u0645\u0627\u0644", None))
        self.report_tab.setTabText(self.report_tab.indexOf(self.class_report_tab), QCoreApplication.translate("MainWindow", u"\u06a9\u0644\u0627\u0633", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f \u0645\u0644\u06cc:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645:", None))
        self.stu_report_firstName_lineEdit.setInputMask("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc :", None))
        self.stu_report_lastName_lineEdit.setInputMask("")
        self.stu_report_search_btn.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a\u062c\u0648", None))
        self.stu_detail_firstName_lineEdit.setInputMask("")
        self.stu_detail_lastName_lineEdit.setInputMask("")
        self.stu_detail_className_lineEdit.setInputMask("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0632 \u062a\u0627\u0631\u06cc\u062e:", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627 \u062a\u0627\u0631\u06cc\u062e:", None))
        self.stu_report_status_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0647\u0645\u0647", None))
        self.stu_report_status_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u062d\u0627\u0636\u0631", None))
        self.stu_report_status_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u063a\u0627\u06cc\u0628", None))
        self.stu_report_status_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u062a\u0627\u062e\u06cc\u0631", None))

        self.stu_report_show_report_btn.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0645\u0627\u06cc\u0634", None))
        self.report_tab.setTabText(self.report_tab.indexOf(self.student_report_tab), QCoreApplication.translate("MainWindow", u"\u062f\u0627\u0646\u0634 \u0622\u0645\u0648\u0632", None))
        self.sms_class_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0647\u0645\u0647", None))

        self.sms_class_comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"\u0647\u0645\u0647", None))
        self.stu_report_lastName_lineEdit_2.setInputMask("")
        self.stu_report_firstName_lineEdit_2.setInputMask("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc :", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645:", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f \u0645\u0644\u06cc:", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0644\u0627\u0633 :", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0633\u062a\u062c\u0648", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0631\u0633\u0627\u0644", None))
        self.sms_tab.setTabText(self.sms_tab.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u063a\u0627\u06cc\u0628\u06cc\u0646", None))
        self.class_report_comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0647\u0645\u0647", None))

        self.class_report_comboBox_3.setCurrentText(QCoreApplication.translate("MainWindow", u"\u0647\u0645\u0647", None))
        self.stu_report_lastName_lineEdit_3.setInputMask("")
        self.stu_report_firstName_lineEdit_3.setInputMask("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc :", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645:", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0644\u0627\u0633 :", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f \u0645\u0644\u06cc:", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.sms_tab.setTabText(self.sms_tab.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u062a\u0627\u062e\u06cc\u0631\u0647\u0627", None))
        self.class_report_comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0647\u0645\u0647", None))

        self.class_report_comboBox_4.setCurrentText(QCoreApplication.translate("MainWindow", u"\u0647\u0645\u0647", None))
        self.stu_report_lastName_lineEdit_4.setInputMask("")
        self.stu_report_firstName_lineEdit_4.setInputMask("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc :", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0627\u0631\u06cc\u062e:", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645:", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0644\u0627\u0633 :", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u062f \u0645\u0644\u06cc:", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.sms_tab.setTabText(self.sms_tab.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u0628\u06cc \u0627\u0646\u0638\u0628\u0627\u0637\u06cc", None))
        self.pic_main.setText("")
        self.main_btn.setText(QCoreApplication.translate("MainWindow", u"\u0635\u0641\u062d\u0647 \u0627\u0635\u0644\u06cc ", None))
        self.manager_btn.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062f\u06cc\u0631\u06cc\u062a", None))
        self.attandance_btn.setText(QCoreApplication.translate("MainWindow", u"\u062b\u0628\u062a \u0648\u0636\u0639\u06cc\u062a", None))
        self.report_btn.setText(QCoreApplication.translate("MainWindow", u"\u06af\u0632\u0627\u0631\u0634", None))
        self.sms_btn.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0637\u0644\u0627\u0639 \u0631\u0633\u0627\u0646\u06cc", None))
    # retranslateUi

