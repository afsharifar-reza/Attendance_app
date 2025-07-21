import os
import sys

# اضافه کردن مسیر پروژه اصلی به sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap
from ui.ui_dashboard import Ui_MainWindow
from front_end.class_manager import ClassManager



class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        # تنظیم رابط کاربری
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pic_main.setPixmap(QPixmap("front_end/picture/logo.png"))

        # تنظیم صفحه اولیه
        self.ui.stackedWidget_dashboard.setCurrentIndex(0)

        # ساخت شیء مدل کلاس‌ها
        try:
            self.class_manager = ClassManager(self.ui)  # بدون نیاز به ارسال connection
        except Exception as e:
            QMessageBox.critical(self, "خطا", f"خطا در راه‌اندازی سیستم: {str(e)}")
            sys.exit(1)

        # اتصال سیگنال‌ها
        self.ui.main_btn.clicked.connect(self.show_main_page)
        self.ui.manager_btn.clicked.connect(self.show_manager_page)
        self.ui.sub_btn.clicked.connect(self.class_manager.add_new_class)



    def show_main_page(self):
        self.ui.stackedWidget_dashboard.setCurrentIndex(0)

    def show_manager_page(self):
        self.ui.stackedWidget_dashboard.setCurrentIndex(1)
        self.ui.mange_tab.setCurrentIndex(0)
        self.class_manager. load_classes()


if __name__ == "__main__":
    app = QApplication([])
    window = Dashboard()
    window.show()
    app.exec()
