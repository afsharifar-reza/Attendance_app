import os
import sys

# اضافه کردن مسیر پروژه اصلی به sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap
from ui.ui_dashboard import Ui_MainWindow
from PySide6.QtCore import Qt
from front_end.class_manager import ClassManager
from front_end.student_manager import StudentManager
from front_end.attendance_manager import AttendanceManager


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

        # ساخت شیء مدل کلاس‌ها
        try:
            self.class_manager = ClassManager(self.ui)  # بدون نیاز به ارسال connection
            self.student_manager = StudentManager(self.ui) 
            self.attendance_manager=AttendanceManager(self.ui)
        except Exception as e:
            print(f"{__name__} : {str(e)}")
            QMessageBox.critical(self, "خطا", f"خطا در راه‌اندازی سیستم: {str(e)}")
            sys.exit(1)

        # اتصال سیگنال‌ها
        self.ui.main_btn.clicked.connect(self.show_main_page)
        self.ui.manager_btn.clicked.connect(self.show_manager_page)
        self.ui.attandance_btn.clicked.connect(self.show_attandance_page)
        



    def show_main_page(self):
        self.ui.stackedWidget_dashboard.setCurrentIndex(0)

    def show_manager_page(self):
        self.ui.stackedWidget_dashboard.setCurrentIndex(1)
        self.ui.mange_tab.setCurrentIndex(0)
        
    
    def check_tab_change(self, index):
        print(f"{__name__} tab index= {index} ")
        if index == 0:  # اگر تب سوم فعال شد
            self.class_manager.load_classes()
        elif index == 1:
            self.ui.sub_btn.clicked.connect(self.class_manager.add_new_class)
        elif index==2:    
            self.class_manager.load_classes_into_combobox(self.ui.class_comboBox)
            self.ui.submit_student_btn.clicked.connect(self.student_manager.validate_and_submit)
        elif index==3:
            self.student_manager.setup_table_headers()
            self.class_manager.load_classes_into_combobox(self.ui.class_comboBox_2)
            self.ui.searchButton.clicked.connect(self.student_manager.search_students)
            self.ui.studentTableView.clicked.connect(self.student_manager.on_table_row_selected)
            self.ui.update_student_btn.clicked.connect(self.student_manager.validate_and_update)
    

    def show_attandance_page(self):
        self.ui.stackedWidget_dashboard.setCurrentIndex(2)
        self.class_manager.load_classes_into_combobox(self.ui.class_comboBox_3)
        self.ui.loadButton.clicked.connect(self.attendance_manager.load_attendance_table)
        self.ui.cancelButton.clicked.connect(self.attendance_manager.load_attendance_table)
        self.ui.saveButton.clicked.connect(self.attendance_manager.save_attendance_table)
        


    
           






if __name__ == "__main__":
    app = QApplication([])
    window = Dashboard()
    window.show()
    app.exec()
