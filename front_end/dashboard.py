import os
import sys

# اضافه کردن مسیر پروژه اصلی به sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtGui import QPixmap
from ui.ui_dashboard import Ui_MainWindow
from back_end.models.class_model import ClassModel


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
        self.class_model = ClassModel()
        self.class_model.create_table()  # در صورت عدم وجود، جدول را بسازد

        # اتصال سیگنال‌ها
        self.ui.main_btn.clicked.connect(self.show_main_page)
        self.ui.manager_btn.clicked.connect(self.show_manager_page)
        self.ui.sub_btn.clicked.connect(self.add_new_class)

    def add_new_class(self):
        grade = self.ui.Grade_comboBox.currentText().strip()
        field = self.ui.Field_comboBox.currentText().strip()

        if not grade or not field:
            QMessageBox.warning(self, "خطا", "لطفاً پایه و رشته را انتخاب کنید.")
            return

        success = self.class_model.add_class(grade, field)
        if success:
            QMessageBox.information(self, "موفقیت", f"کلاس {grade} {field} ثبت شد.")
            self.load_classes_into_table()
        else:
            QMessageBox.warning(self, "تکراری", "این کلاس قبلاً ثبت شده است.")

    def load_classes_into_table(self):
        class_list = self.class_model.get_all_classes()
        table = self.ui.class_tableWidget

        table.setRowCount(len(class_list))
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["پایه", "رشته", "نام کلاس"])

        for row, (_, grade, field, name) in enumerate(class_list):
            table.setItem(row, 0, QTableWidgetItem(grade))
            table.setItem(row, 1, QTableWidgetItem(field))
            table.setItem(row, 2, QTableWidgetItem(name))

    def show_main_page(self):
        self.ui.stackedWidget_dashboard.setCurrentIndex(0)

    def show_manager_page(self):
        self.ui.stackedWidget_dashboard.setCurrentIndex(1)
        self.ui.mange_tab.setCurrentIndex(0)
        self.load_classes_into_table()


if __name__ == "__main__":
    app = QApplication([])
    window = Dashboard()
    window.show()
    app.exec()
