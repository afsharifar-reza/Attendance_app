from PySide6.QtWidgets import QMessageBox
from back_end.models.student_model import StudentModel
from back_end.models.class_model import ClassModel

class StudentManager:
    def __init__(self, ui):

        self.ui = ui
        try:
            self.student_model = StudentModel()
            self.class_model = ClassModel()
        except ConnectionError as e:
            QMessageBox.critical(None, "خطای دیتابیس", f"خطا در اتصال به دیتابیس: {str(e)}")
            raise
        except Exception as e:
            QMessageBox.critical(None, "خطای سیستمی", f"خطای غیرمنتظره: {str(e)}")
            raise

    def validate_and_submit(self):
        """اعتبارسنجی و ثبت دانش آموز جدید"""
        # دریافت مقادیر از UI
        selected_class = self.ui.class_comboBox.currentText()  # نام کلاس انتخاب شده
        class_id = self._get_class_id(selected_class)  # تبدیل نام کلاس به ID
        
        if class_id is None:
            QMessageBox.warning(None, "خطا", "کلاس انتخاب شده معتبر نیست")
            return

        data = {
            'student_id': self.ui.student_id_lineEdit.text().strip(),
            'first_name': self.ui.first_name_lineEdit.text().strip(),
            'last_name': self.ui.last_name_lineEdit.text().strip(),
            'father_name': self.ui.father_name_lineEdit.text().strip(),
            'class_id': class_id,  # استفاده از class_id استخراج شده
            'parent_phone': self.ui.parent_phone_lineEdit.text().strip()
        }

        # بقیه کدهای اعتبارسنجی و ثبت بدون تغییر...
        if not self._validate_fields(data):
            return

        try:
            self.student_model.add_student(**data)
            QMessageBox.information(None, "موفق", "دانش آموز با موفقیت ثبت شد")
            self._clear_form()
        except Exception as e:
            QMessageBox.critical(None, "خطا", f"خطا در ثبت دانش آموز: {str(e)}")

    def _get_class_id(self, class_name):
        """تبدیل نام کلاس به class_id از دیتابیس"""
        try:
            classes = self.class_model.get_all_classes()
            for cls in classes:
                if cls[3] == class_name:  # فرض: cls[0]=id, cls[1]=name
                    print(cls[0])
                    return cls[0]
            return None
        except Exception as e:
            QMessageBox.critical(None, "خطا", f"خطا در دریافت اطلاعات کلاس: {str(e)}")
            return None
        


    def _validate_fields(self, data):
        """اعتبارسنجی فیلدهای ورودی"""
        # بررسی فیلدهای اجباری
        required_fields = {
            'student_id': 'کد ملی',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'father_name': 'نام پدر',
            'class_id': 'کلاس'
        }
        
        for field, name in required_fields.items():
            if not data.get(field):
                QMessageBox.warning(None, "خطا", f"فیلد {name} الزامی است")
                return False

        # بررسی کد ملی (10 رقم)
        if len(data['student_id']) != 10 or not data['student_id'].isdigit():
            QMessageBox.warning(None, "خطا", "کد ملی باید 10 رقم باشد")
            return False

        # بررسی شماره تماس (11 رقم - اختیاری)
        if data['parent_phone'] and (len(data['parent_phone']) != 11 or not data['parent_phone'].isdigit()):
            QMessageBox.warning(None, "خطا", "شماره تماس باید 11 رقم باشد")
            return False

        return True

    def _clear_form(self):
        """پاک کردن فرم پس از ثبت موفق"""
        self.ui.student_id_lineEdit.clear()
        self.ui.first_name_lineEdit.clear()
        self.ui.last_name_lineEdit.clear()
        self.ui.father_name_lineEdit.clear()
        self.ui.parent_phone_lineEdit.clear()