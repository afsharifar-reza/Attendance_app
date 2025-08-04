from PySide6.QtWidgets import QMessageBox, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from back_end.models.student_model import StudentModel
from back_end.models.attendance_model import AttendanceModel
from persiantools.jdatetime import JalaliDate
from datetime import datetime
import re

class StudentReportManager:
    def __init__(self, ui):
        self.ui = ui
        self.student_model = StudentModel()
        self.attendance_model = AttendanceModel()
        self.setup_table()
        self.setup_report_table()

    def setup_table(self):
        self.headers = ["کد ملی", "نام", "نام خانوادگی", "نام پدر", "کلاس", "شماره تماس"]
        self.table_model = QStandardItemModel(0, len(self.headers))
        self.table_model.setHorizontalHeaderLabels(self.headers)

        self.ui.search_table_view.setModel(self.table_model)
        self.ui.search_table_view.horizontalHeader().setStretchLastSection(True)
        self.ui.search_table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.search_table_view.setAlternatingRowColors(True)

    def search_students(self):
        first_name = self.ui.stu_report_firstName_lineEdit.text().strip()
        last_name = self.ui.stu_report_lastName_lineEdit.text().strip()
        student_id = self.ui.stu_report_nationalCode_lineEdit.text().strip()

        try:
            results = self.student_model.search_students_with_classname(
                first_name=first_name,
                last_name=last_name,
                student_id=student_id
            )
            self.populate_table(results)
        except Exception as e:
            QMessageBox.critical(None, "خطا", f"خطا در جستجوی دانش‌آموزان:\n{e}")

    def populate_table(self, data):
        self.table_model.setRowCount(0)
        for row in data:
            items = [QStandardItem(str(cell)) for cell in row]
            self.table_model.appendRow(items)
        self.ui.search_table_view.resizeRowsToContents()

    def handle_student_row_click(self, index):
        row = index.row()

        student_id = self.table_model.item(row, 0).text()
        first_name = self.table_model.item(row, 1).text()
        last_name = self.table_model.item(row, 2).text()
        father_name = self.table_model.item(row, 3).text()
        class_name = self.table_model.item(row, 4).text()
        parent_phone = self.table_model.item(row, 5).text()

        self.ui.stu_detail_nationalCode_lineEdit.setText(student_id)
        self.ui.stu_detail_firstName_lineEdit.setText(first_name)
        self.ui.stu_detail_lastName_lineEdit.setText(last_name)
        self.ui.stu_detail_className_lineEdit.setText(class_name)

        self.selected_student_data = {
            "student_id": student_id,
            "first_name": first_name,
            "last_name": last_name,
            "father_name": father_name,
            "class_name": class_name,
            "parent_phone": parent_phone
        }

    def setup_report_table(self):
        self.headers = ["تاریخ", "ساعت 1", "ساعت 2", "ساعت 3", "ساعت 4", "تاخیر"]
        self.report_table_model = QStandardItemModel(0, len(self.headers))
        self.report_table_model.setHorizontalHeaderLabels(self.headers)

        self.ui.stu_report_tableView.setModel(self.report_table_model)
        self.ui.stu_report_tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.stu_report_tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.stu_report_tableView.setAlternatingRowColors(True)

    def is_valid_jalali_date(self, date_str):
        return re.match(r"^14\d{2}-\d{2}-\d{2}$", date_str)
    
    def show_student_attendance_report(self):
        print(f"{__name__} : report is good ")
        if not hasattr(self, 'selected_student_data') or not self.selected_student_data:
            QMessageBox.warning(None, "هشدار", "لطفاً ابتدا یک دانش‌آموز را از جدول انتخاب کنید.")
            return

        start_date_text = self.ui.stu_report_from_dateEdit.text().strip()
        end_date_text = self.ui.stu_report_to_dateEdit.text().strip()
        selected_status = self.ui.stu_report_status_comboBox.currentText()
        student_id = self.selected_student_data['student_id']

        if not start_date_text or not end_date_text:
            QMessageBox.warning(None, "خطا", "لطفاً بازه زمانی را کامل وارد کنید.")
            return

        if not self.is_valid_jalali_date(start_date_text) or not self.is_valid_jalali_date(end_date_text):
            QMessageBox.warning(None, "خطا", "فرمت تاریخ باید همانند 1404-04-04 باشد.")
            return

        try:
            start_date = JalaliDate(*map(int, start_date_text.split("-"))).to_gregorian()
            end_date = JalaliDate(*map(int, end_date_text.split("-"))).to_gregorian()
        except Exception as e:
            QMessageBox.critical(None, "خطا", f"تبدیل تاریخ با خطا مواجه شد:\n{e}")
            return

        records = self.attendance_model.get_attendance_report_by_student(student_id, start_date, end_date)
        self.report_table_model.setRowCount(0)

        for record in records:
            date, hour1, hour2, hour3, hour4, delay = record

            # تبدیل رشته به عدد
            try:
                statuses = [int(hour1), int(hour2), int(hour3), int(hour4)]
            except ValueError:
                continue  # اگر خطا در تبدیل بود، از این رکورد بگذر

            # اعمال فیلتر وضعیت انتخابی
            if selected_status == "حاضر":
                if not all(s == 1 for s in statuses):
                    continue
            elif selected_status == "غایب":
                if not any(s == 0 for s in statuses):
                    continue
            elif selected_status == "تاخیر":
                if not any(s == 2 for s in statuses):
                    continue


            try:
                # اگر تاریخ به‌صورت datetime یا str باشه
                if isinstance(date, datetime):
                    date_shamsi = JalaliDate.to_jalali(date).strftime("%Y/%m/%d")
                else:
                    date_obj = datetime.fromisoformat(date)
                    date_shamsi = JalaliDate.to_jalali(date_obj).strftime("%Y/%m/%d")
            except Exception as e:
                print(f"[!] خطا در تبدیل تاریخ: {e}")
                date_shamsi = str(date)


            row = [
                QStandardItem(date_shamsi),
                QStandardItem(self.status_to_text(hour1)),
                QStandardItem(self.status_to_text(hour2)),
                QStandardItem(self.status_to_text(hour3)),
                QStandardItem(self.status_to_text(hour4)),
                QStandardItem(f"{delay} دقیقه") if int(delay) > 0 else QStandardItem("-")
            ]

            self.report_table_model.appendRow(row)






    def status_to_text(self, status):
        try:
            status = int(status)
        except:
            return "نامشخص"

        if status == 0:
            return "غایب"
        elif status == 1:
            return "حاضر"
        elif status == 2:
            return "تاخیر"
        else:
            return "نامشخص"

