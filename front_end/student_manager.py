
from PySide6.QtWidgets import QMessageBox, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from back_end.models.student_model import StudentModel
from back_end.models.class_model import ClassModel

class StudentManager:
    def __init__(self, ui):
        self.ui = ui

        try:
            self.student_model = StudentModel()
            self.class_model = ClassModel()


        except Exception as e:
            QMessageBox.critical(None, "خطای سیستمی", f"خطای غیرمنتظره:\n{str(e)}")
            raise

    def validate_and_submit(self):
        """دریافت، اعتبارسنجی و ثبت اطلاعات دانش‌آموز"""

        # 1. دریافت اطلاعات از فرم
        data = {
            'student_id': self.ui.student_id_lineEdit.text().strip(),
            'first_name': self.ui.first_name_lineEdit.text().strip(),
            'last_name': self.ui.last_name_lineEdit.text().strip(),
            'father_name': self.ui.father_name_lineEdit.text().strip(),
            'parent_phone': self.ui.parent_phone_lineEdit.text().strip(),
            'class_id': self._get_class_id(self.ui.class_comboBox.currentText().strip())
        }

        # 2. اعتبارسنجی اطلاعات
        if not self._validate_fields(data):
            return

        # 3. بررسی تکراری نبودن کد ملی
        if self._is_student_id_duplicate(data['student_id']):
            QMessageBox.warning(None, "تکرار", "دانش‌آموزی با این کد ملی قبلاً ثبت شده است.")
            return

        # 4. ذخیره در پایگاه داده
        success = self.student_model.add_student(**data)

        if success:
            QMessageBox.information(None, "موفقیت", "دانش‌آموز با موفقیت ثبت شد.")
            self._clear_form()
        else:
            QMessageBox.warning(None, "خطا", "ثبت دانش‌آموز با خطا مواجه شد. ممکن است کد ملی تکراری باشد یا مشکلی در دیتابیس وجود داشته باشد.")

    def validate_and_update(self):
        """دریافت، اعتبارسنجی و ثبت اطلاعات دانش‌آموز"""

        # 1. دریافت اطلاعات از فرم
        data = {
            'student_id': self.ui.nationalCodeEditLineEdit.text().strip(),
            'first_name': self.ui.firstNameEditLineEdit.text().strip(),
            'last_name': self.ui.lastNameEditLineEdit.text().strip(),
            'father_name': self.ui.fatherNameEditLineEdit.text().strip(),
            'parent_phone': self.ui.phoneNumberEditLineEdit.text().strip(),
            'class_id': self._get_class_id(self.ui.class_comboBox_2.currentText().strip())
        }

        # 2. اعتبارسنجی اطلاعات
        if not self._validate_fields(data):
            return
        # 4. ذخیره در پایگاه داده
        success = self.student_model.update_student(**data)

        if success:
            QMessageBox.information(None, "موفقیت", "دانش‌آموز با موفقیت ویرایش شد.")
            self._clear_updat_form()
        else:
            QMessageBox.warning(None, "خطا", "ویرایش با خطا مواجه شد.")

    def _get_class_id(self, class_name: str):
        """تبدیل نام کلاس به شناسه کلاس از دیتابیس"""
        try:
            for cls in self.class_model.get_all_classes():
                if cls[3] == class_name:  # فرض بر این است که ستون ۳ نام کلاس است
                    return cls[0]        # ستون ۰ شناسه کلاس
            return None
        except Exception as e:
            QMessageBox.critical(None, "خطا", f"خطا در دریافت اطلاعات کلاس:\n{str(e)}")
            return None

    def _validate_fields(self, data: dict) -> bool:
        """اعتبارسنجی داده‌های ورودی"""

        required_fields = {
            'student_id': 'کد ملی',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'father_name': 'نام پدر',
            'class_id': 'کلاس'
        }

        # 1. بررسی فیلدهای اجباری
        for field, label in required_fields.items():
            if not data.get(field):
                QMessageBox.warning(None, "خطا", f"فیلد «{label}» الزامی است.")
                return False

        # 2. اعتبارسنجی کد ملی (۱۰ رقمی)
        if not (data['student_id'].isdigit() and len(data['student_id']) == 10):
            QMessageBox.warning(None, "خطا", "کد ملی باید شامل ۱۰ رقم باشد.")
            return False

        # 3. اعتبارسنجی شماره تماس والدین (اختیاری - اگر وارد شد ۱۱ رقمی)
        phone = data.get('parent_phone')
        if phone and (not phone.isdigit() or len(phone) != 11):
            QMessageBox.warning(None, "خطا", "شماره تماس باید ۱۱ رقمی باشد.")
            return False

        return True

    def _is_student_id_duplicate(self, student_id: str) -> bool:
        """بررسی تکراری بودن کد ملی در دیتابیس"""
        try:
            cursor = self.student_model.conn.cursor()
            cursor.execute("SELECT 1 FROM Student WHERE student_id = ?", (student_id,))
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"[!] خطا در بررسی کد ملی تکراری: {e}")
            return False  # اگر خطا رخ داد، فرض را بر تکراری نبودن می‌گذاریم

    def _clear_updat_form(self):
        """پاکسازی فرم پس از ثبت موفق"""
        self.ui.nationalCodeEditLineEdit.clear()
        self.ui.firstNameEditLineEdit.clear()
        self.ui.lastNameEditLineEdit.clear()
        self.ui.fatherNameEditLineEdit.clear()
        self.ui.phoneNumberEditLineEdit.clear()


    def _clear_form(self):
        """پاکسازی فرم پس از ثبت موفق"""
        self.ui.student_id_lineEdit.clear()
        self.ui.first_name_lineEdit.clear()
        self.ui.last_name_lineEdit.clear()
        self.ui.father_name_lineEdit.clear()
        self.ui.parent_phone_lineEdit.clear()

    def search_students(self):
        # گرفتن مقادیر از ورودی‌ها
        first_name = self.ui.firstNameSearchLineEdit.text().strip()
        last_name = self.ui.lastNameSearchLineEdit.text().strip()
        student_id = self.ui.nationalCodeSearchLineEdit.text().strip()

        # دریافت نتایج از مدل
        results = self.student_model.search_students(
            first_name=first_name,
            last_name=last_name,
            student_id=student_id
        )

        # پر کردن جدول با نتایج
        self.fill_table(results)

    def setup_table_headers(self):
        self.table_headers = ["کد ملی", "نام", "نام خانوادگی", "نام پدر", "کلاس", "شماره تماس"]
        self.table_model = QStandardItemModel(0, len(self.table_headers))
        self.table_model.setHorizontalHeaderLabels(self.table_headers)
        
        self.ui.studentTableView.setModel(self.table_model)
        
        # تنظیمات نمایشی
        self.ui.studentTableView.horizontalHeader().setStretchLastSection(True)
        self.ui.studentTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.studentTableView.setAlternatingRowColors(True)

    def fill_table(self, data):
        self.table_model.setRowCount(0)  # پاک‌کردن ردیف‌ها قبلی

        for row in data:
            row_items = []
            for value in row:
                item = QStandardItem(str(value) if value is not None else "")
                
                row_items.append(item)
            self.table_model.appendRow(row_items)

        self.ui.studentTableView.resizeRowsToContents()


    def on_table_row_selected(self, index):
        if not index.isValid():
            return

        model = self.ui.studentTableView.model()
        row = index.row()

        self.ui.nationalCodeEditLineEdit.setText(model.index(row, 0).data())
        self.ui.firstNameEditLineEdit.setText(model.index(row, 1).data())
        self.ui.lastNameEditLineEdit.setText(model.index(row, 2).data())
        self.ui.fatherNameEditLineEdit.setText(model.index(row, 3).data())
        self.ui.class_comboBox_2.setCurrentText(model.index(row, 4).data())
        self.ui.phoneNumberEditLineEdit.setText(model.index(row, 5).data())

