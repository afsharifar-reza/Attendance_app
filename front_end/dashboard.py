import os
import sys

# اضافه کردن مسیر پروژه اصلی به sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox,QComboBox
from PySide6.QtGui import QPixmap
from ui.ui_dashboard import Ui_MainWindow
from PySide6.QtCore import Qt
from front_end.class_manager import ClassManager
from front_end.student_manager import StudentManager
from front_end.attendance_manager import AttendanceManager
from front_end.report_manager import ReportManager
from front_end.stu_report_manager import StudentReportManager

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        # تنظیم رابط کاربری
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pic_main.setPixmap(QPixmap("front_end/picture/logo.png"))

        # تنظیم صفحه اولیه
        self.ui.stackedWidget_dashboard.setCurrentIndex(0)
        self.ui.mange_tab.currentChanged.connect(self.check_tab_change)
        self.ui.report_tab.currentChanged.connect(self.check_report_tab_change)

        # فلگ‌ها برای جلوگیری از اتصال‌های تکراری
        # self.attendance_manager_tab=False
        self.report_student_tab_connected = False
        self.report_class_tab_connected = False
        self.class_tab_connected = False
        self.add_class_tab_connected = False
        self.student_add_tab_connected = False
        self.student_edit_tab_connected = False
        

        # ساخت شیء مدل‌ها
        try:
            self.class_manager = ClassManager(self.ui)
            self.student_manager = StudentManager(self.ui)
            self.attendance_manager = AttendanceManager(self.ui)
            self.report_manager = ReportManager(self.ui)
            self.stu_report_manager = StudentReportManager(self.ui)
        except Exception as e:
            print(f"{__name__} : {str(e)}")
            QMessageBox.critical(self, "خطا", f"خطا در راه‌اندازی سیستم: {str(e)}")
            sys.exit(1)

        # اتصال سیگنال‌های صفحه اصلی
        self.ui.main_btn.clicked.connect(self.show_main_page)
        self.ui.manager_btn.clicked.connect(self.show_manager_page)
        self.ui.attandance_btn.clicked.connect(self.show_attandance_page)
        self.ui.report_btn.clicked.connect(self.show_report_page)
        self.ui.sms_btn.clicked.connect(self.show_sms_page)

        # اجرای اولیه عملکرد تب فعال
        self.check_tab_change(self.ui.mange_tab.currentIndex())
        self.check_report_tab_change(self.ui.report_tab.currentIndex())

    def show_main_page(self):
        self.ui.stackedWidget_dashboard.setCurrentIndex(0)

    def show_manager_page(self):
        self.ui.stackedWidget_dashboard.setCurrentIndex(1)
        self.ui.mange_tab.setCurrentIndex(0)


    def check_tab_change(self, index):
        print(f"{__name__} tab index= {index} ")
        if index == 0:
            if not self.class_tab_connected:
                self.class_manager.load_classes()
                self.class_tab_connected = True

        elif index == 1:
            if not self.add_class_tab_connected:
                self.ui.sub_btn.clicked.connect(self.class_manager.add_new_class)
                self.add_class_tab_connected = True

        elif index == 2:
            if not self.student_add_tab_connected:
                self.class_manager.load_classes_into_combobox(self.ui.class_comboBox)
                self.ui.submit_student_btn.clicked.connect(self.student_manager.validate_and_submit)
                self.student_add_tab_connected = True

        elif index == 3:
            if not self.student_edit_tab_connected:
                self.student_manager.setup_table_headers()
                self.class_manager.load_classes_into_combobox(self.ui.class_comboBox_2)
                self.ui.searchButton.clicked.connect(self.student_manager.search_students)
                self.ui.studentTableView.clicked.connect(self.student_manager.on_table_row_selected)
                self.ui.update_student_btn.clicked.connect(self.student_manager.validate_and_update)
                self.student_edit_tab_connected = True



    def show_attandance_page(self):
       
        self.ui.stackedWidget_dashboard.setCurrentIndex(2)
        self.class_manager.load_classes_into_combobox(self.ui.class_comboBox_3)
        self.ui.loadButton.clicked.connect(self.attendance_manager.load_attendance_table)
        self.ui.cancelButton.clicked.connect(self.attendance_manager.load_attendance_table)
        self.ui.saveButton.clicked.connect(self.attendance_manager.save_attendance_table)
       

    def show_report_page(self):
        self.ui.stackedWidget_dashboard.setCurrentIndex(3)
        self.ui.report_tab.setCurrentIndex(0)
        self.class_manager.load_classes_into_combobox(self.ui.class_report_comboBox)

    def check_report_tab_change(self, index):
        print(f"{__name__} tab index= {index} ")
        if index == 0:
            if not self.report_class_tab_connected:
                self.ui.class_report_btn.clicked.connect(self.report_manager.generate_class_report)
                self.report_class_tab_connected = True
        elif index == 1:
            if not self.report_student_tab_connected:
                self.stu_report_manager.setup_table()
                self.stu_report_manager.setup_report_table()
                self.ui.stu_report_search_btn.clicked.connect(self.stu_report_manager.search_students)
                self.ui.search_table_view.clicked.connect(self.stu_report_manager.handle_student_row_click)
                self.ui.stu_report_show_report_btn.clicked.connect(self.stu_report_manager.show_student_attendance_report)
                self.report_student_tab_connected = True  # اتصال فقط یک‌بار انجام می‌شود


    def show_sms_page(self):
        self.ui.stackedWidget_dashboard.setCurrentIndex(4)
        self.ui.sms_tab.setCurrentIndex(0)
        self.class_manager.load_classes_into_combobox(self.ui.sms_class_comboBox)
        self.ui.sms_class_comboBox.addItem("همه")



if __name__ == "__main__":
    app = QApplication([])
    window = Dashboard()
    window.show()
    app.exec()
