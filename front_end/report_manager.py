from PySide6.QtWidgets import QMessageBox, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from persiantools.jdatetime import JalaliDate
from datetime import datetime
from collections import defaultdict
import locale
import re

from back_end.models.student_model import StudentModel
from back_end.models.attendance_model import AttendanceModel
from back_end.models.class_model import ClassModel

# فعال کردن مرتب‌سازی فارسی
locale.setlocale(locale.LC_ALL, '')

class ReportManager:
    def __init__(self, ui):
        self.ui = ui
        self.init_models()
        self.init_report_table()

    def init_models(self):
        try:
            self.student_model = StudentModel()
            self.attendance_model = AttendanceModel()
            self.class_model = ClassModel()
        except ConnectionError as e:
            QMessageBox.critical(None, "خطای دیتابیس", f"خطا در اتصال به پایگاه داده:\n{str(e)}")
            raise

    def init_report_table(self):
        self.report_class_model_view = QStandardItemModel()
        headers = ["کد ملی", "نام", "نام خانوادگی", "پیش‌نمایش"]
        self.report_class_model_view.setHorizontalHeaderLabels(headers)
        self.ui.class_report_table.setModel(self.report_class_model_view)

        view = self.ui.class_report_table
        view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        view.setAlternatingRowColors(True)

    def is_valid_jalali_date(self, date_str):
        return re.match(r"^14\d{2}-\d{2}-\d{2}$", date_str)

    def generate_class_report(self):
        class_name = self.ui.class_report_comboBox.currentText().strip()
        start_date_text = self.ui.start_class_dateEdit.text().strip()
        end_date_text = self.ui.end_class_dateEdit.text().strip()

        if not class_name or not start_date_text or not end_date_text:
            QMessageBox.warning(None, "خطا", "لطفاً کلاس و بازه زمانی را کامل وارد کنید.")
            return

        if not self.is_valid_jalali_date(start_date_text) or not self.is_valid_jalali_date(end_date_text):
            QMessageBox.warning(None, "خطا", "فرمت تاریخ باید به صورت 1404-04-25 باشد.")
            return

        try:
            start_parts = list(map(int, start_date_text.split("-")))
            end_parts = list(map(int, end_date_text.split("-")))
            start_date = str(JalaliDate(*start_parts).to_gregorian())
            end_date = str(JalaliDate(*end_parts).to_gregorian())
        except Exception as e:
            QMessageBox.warning(None, "خطا", f"تبدیل تاریخ شمسی به میلادی با خطا مواجه شد:\n{str(e)}")
            return

        class_id = self._get_class_id(class_name)
        if not class_id:
            QMessageBox.critical(None, "خطا", "کلاس مورد نظر یافت نشد.")
            return

        rows = self.attendance_model.get_attendance_report_by_class(class_id, start_date, end_date)

        students_data = defaultdict(lambda: {
            'first_name': '',
            'last_name': '',
            'national_code': '',
            'records': {},
            'absent_hours': 0,
            'delay_minutes': 0
        })

        date_set = set()

        for row in rows:
            student_id, fname, lname, date, h1, h2, h3, h4, delay = row
            summary = ' '.join([
                self._status_map(h1),
                self._status_map(h2),
                self._status_map(h3),
                self._status_map(h4)
            ])
            absent_count = [h1, h2, h3, h4].count("0")
            students_data[student_id]['first_name'] = fname
            students_data[student_id]['last_name'] = lname
            students_data[student_id]['national_code'] = student_id
            students_data[student_id]['records'][date] = summary
            students_data[student_id]['absent_hours'] += absent_count
            students_data[student_id]['delay_minutes'] += int(delay)
            date_set.add(date)

        date_list = sorted(date_set)
        jalali_dates = [JalaliDate(datetime.strptime(d, "%Y-%m-%d")).strftime("%Y/%m/%d") for d in date_list]

        model = QStandardItemModel()
        headers = ["کد ملی", "نام", "نام خانوادگی"] + jalali_dates + ["ساعات غیبت", "دقایق تأخیر"]
        model.setHorizontalHeaderLabels(headers)

        sorted_students = sorted(students_data.items(), key=lambda x: locale.strxfrm(x[1]['last_name']))

        for _, info in sorted_students:
            row = [
                QStandardItem(info['national_code']),
                QStandardItem(info['first_name']),
                QStandardItem(info['last_name']),
            ]
            for date in date_list:
                summary = info['records'].get(date, "")
                row.append(QStandardItem(summary))
            row.append(QStandardItem(str(info['absent_hours'])))
            row.append(QStandardItem(str(info['delay_minutes'])))
            model.appendRow(row)

        self.ui.class_report_table.setModel(model)
        self.ui.class_report_table.resizeColumnsToContents()
        self.ui.class_report_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def _status_map(self, status):
        return {
            "0": "غ",
            "1": "ح",
            "2": "ت"
        }.get(status, "-")

    def _get_class_id(self, class_name: str):
        try:
            for cls in self.class_model.get_all_classes():
                if cls[3] == class_name:
                    return cls[0]
            return None
        except Exception as e:
            QMessageBox.critical(None, "خطا", f"خطا در دریافت اطلاعات کلاس:\n{str(e)}")
            return None
