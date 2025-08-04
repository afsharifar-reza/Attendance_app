from PySide6.QtWidgets import QMessageBox, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from back_end.models.student_model import StudentModel
from back_end.models.attendance_model import AttendanceModel
from back_end.models.class_model import ClassModel
from persiantools.jdatetime import JalaliDate

import re

class AbsentSmseManager:
    def __init__(self, ui):
        self.ui = ui
        self.init_modles()
        self.absent_table()

    def init_modles(self):
        try:
            self.student_model = StudentModel()
            self.attendance_model = AttendanceModel()
            self.class_model=ClassModel()
        except ConnectionError as e:
            QMessageBox.critical(None, "خطای دیتابیس", f"خطا در اتصال به پایگاه داده:\n{str(e)}")
            raise

    def absent_table(self):
        self.headers = ["کد ملی", "نام", "نام خانوادگی", "نام پدر", "کلاس","وضعیت", "شماره تماس","پیامک"]
        self.table_model = QStandardItemModel(0, len(self.headers))
        self.table_model.setHorizontalHeaderLabels(self.headers)

        self.ui.absent_table_view.setModel(self.table_model)
        self.ui.absent_table_view.horizontalHeader().setStretchLastSection(True)
        self.ui.absent_table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.absent_table_view.setAlternatingRowColors(True)

    
    def is_valid_jalali_date(self, date_str):
        return re.match(r"^14\d{2}-\d{2}-\d{2}$", date_str)
    
    def load_absence_report(self):
        self.table_model.removeRows(0, self.table_model.rowCount())
        class_name = self.ui.absence_class_comboBox.currentText().strip()
        date_text = self.ui.absence_date.text().strip()

        # بررسی تاریخ
        if not self.is_valid_jalali_date(date_text):
            QMessageBox.warning(None, "خطا", "فرمت تاریخ باید به صورت 1404-04-25 باشد.")
            return

        # استخراج class_id در صورت انتخاب کلاس خاص
        class_id = None
        if class_name != "همه":
            for c in self.class_model.get_all_classes():
                if c[3] == class_name:
                    class_id = c[0]
                    break

        # دریافت لیست دانش‌آموزانی که غیبت دارند
        try:
            date_text = JalaliDate(*map(int, date_text.split("-"))).to_gregorian()
            
        except Exception as e:
            QMessageBox.critical(None, "خطا", f"تبدیل تاریخ با خطا مواجه شد:\n{e}")
            return


        absent_records = self.attendance_model.get_absent_students_by_date_and_class(date_text, class_id)
        if not absent_records:
            QMessageBox.warning(None, "خطا", "هیچ رکوردی یافت نشد")
            return
        else:

            # برای هر دانش‌آموز، اطلاعات را از StudentModel بگیر
            student_data = []
            for record in absent_records:
                student_id, s1, s2, s3, s4 = record
                student_info = self.student_model.get_student_by_id(student_id)
                if not student_info:
                    continue  # نادیده گرفتن اگر اطلاعات یافت نشد

                # محاسبه وضعیت
                hours_absent = [i+1 for i, s in enumerate([s1, s2, s3, s4]) if int(s) == 0]
                if len(hours_absent) == 4:
                    status_text = "غیبت کامل"
                else:
                    status_text = f"غیبت ساعت {' و '.join(map(str, hours_absent))}"

                student_data.append({
                    "student_id": student_info[0],
                    "first_name": student_info[1],
                    "last_name": student_info[2],
                    "father_name": student_info[3],
                    "class_name": self.class_model.get_class_name_by_id(student_info[4]),
                    "status": status_text,
                    "phone": student_info[5]
                })

        # مرتب‌سازی بر اساس نام خانوادگی
        student_data.sort(key=lambda x: x["last_name"])

        # پر کردن جدول
        for student in student_data:
            row = [
                QStandardItem(student["student_id"]),
                QStandardItem(student["first_name"]),
                QStandardItem(student["last_name"]),
                QStandardItem(student["father_name"]),
                QStandardItem(student["class_name"]),
                QStandardItem(student["status"]),
                QStandardItem(student["phone"]),
                QStandardItem("")  
            ]
            self.table_model.appendRow(row)
