from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from back_end.models.class_model import ClassModel

class ClassManager:
    def __init__(self, ui):
        """
        مقداردهی اولیه با مدیریت خودکار اتصال دیتابیس
        پارامترها:
            ui: رابط کاربری اصلی
        """
        self.ui = ui
        try:
            self.class_model = ClassModel()  # اتصال در ClassModel مدیریت می‌شود
        except ConnectionError as e:
            QMessageBox.critical(None, "خطای دیتابیس", f"خطا در اتصال به دیتابیس: {str(e)}")
            raise
        except Exception as e:
            QMessageBox.critical(None, "خطای سیستمی", f"خطای غیرمنتظره: {str(e)}")
            raise

    def add_new_class(self) -> bool:
        """
        افزودن کلاس جدید با مدیریت خطا
        بازگشت:
            True: عملیات موفق
            False: خطا یا کلاس تکراری
        """
        try:
            grade = self.ui.Grade_comboBox.currentText().strip()
            field = self.ui.Field_comboBox.currentText().strip()

            if not (grade and field):
                QMessageBox.warning(None, "خطا", "لطفاً پایه و رشته را انتخاب کنید.")
                return False

            if self.class_model.add_class(grade, field):
                QMessageBox.information(None, "موفقیت", f"کلاس {grade} {field} ثبت شد.")
                self.load_classes()
                return True
            QMessageBox.warning(None, "تکراری", "این کلاس قبلاً ثبت شده است.")
            return False
            
        except Exception as e:
            QMessageBox.critical(None, "خطا", f"خطای سیستمی: {str(e)}")
            return False

    def load_classes(self) -> None:
        """بارگذاری و نمایش کلاس‌ها در جدول با مدیریت خطا"""
        try:
            classes = self.class_model.get_all_classes()
            table = self.ui.class_tableWidget
            
            table.clearContents()
            table.setRowCount(len(classes))
            table.setHorizontalHeaderLabels(["پایه", "رشته", "نام کلاس"])
            
            for row, (_, grade, field, name) in enumerate(classes):
                table.setItem(row, 0, QTableWidgetItem(grade))
                table.setItem(row, 1, QTableWidgetItem(field))
                table.setItem(row, 2, QTableWidgetItem(name))
                
        except Exception as e:
            QMessageBox.critical(None, "خطا", f"خطا در بارگذاری داده‌ها: {str(e)}")