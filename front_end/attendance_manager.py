# front_end/attendance_manager.py

from PySide6.QtWidgets import QMessageBox, QHeaderView,QAbstractItemView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from persiantools.jdatetime import JalaliDate


from back_end.models.student_model import StudentModel
from back_end.models.attendance_model import AttendanceModel
from back_end.models.class_model import ClassModel
from front_end.delegates.combo_box_delegate import ComboBoxDelegate
from front_end.delegates.spin_box_delegate import SpinBoxDelegate

class AttendanceManager:
    def __init__(self, ui):
        self.ui = ui
        self.init_models()
        self.init_attendance_table()


    

    def init_models(self):
        try:
            self.student_model = StudentModel()
            self.attendance_model = AttendanceModel()
            self.class_model = ClassModel()
        except ConnectionError as e:
            QMessageBox.critical(None, "خطای دیتابیس", f"خطا در اتصال به پایگاه داده:\n{str(e)}")
            raise




        
    def init_attendance_table(self):
        self.table_headers = ["کد ملی", "نام", "نام خانوادگی", "زنگ اول", "زنگ دوم", "زنگ سوم", "زنگ چهارم", "دقایق تأخیر"]
        self.attendance_model_view  = QStandardItemModel(0, len(self.table_headers))
        self.attendance_model_view.setHorizontalHeaderLabels(self.table_headers)
        self.ui.attendanceTableView.setModel(self.attendance_model_view)
        
        # تنظیمات نمایشی
        view = self.ui.attendanceTableView
        view.horizontalHeader().setStretchLastSection(True)
        view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        view.setAlternatingRowColors(True)
        view.setEditTriggers(QAbstractItemView.DoubleClicked)

        # تعریف گزینه‌ها برای هر ستون
        column_options = {
            3: ["حاضر", "غایب", "تاخیر"],  # زنگ اول
            4: ["حاضر", "غایب"],           # زنگ دوم
            5: ["حاضر", "غایب"],           # زنگ سوم
            6: ["حاضر", "غایب"]            # زنگ چهارم
        }

        combo_delegate = ComboBoxDelegate(column_options, view)
        spin_delegate = SpinBoxDelegate(view)

        for col in range(3, 7):
            view.setItemDelegateForColumn(col, combo_delegate)

        view.setItemDelegateForColumn(7, spin_delegate)

        self.non_editable_columns = [0, 1, 2]

       

    
    def load_attendance_table(self):
        # Map عدد به وضعیت
        self.status_map = {
            "0": "غایب",
            "1": "حاضر",
            "2": "تاخیر"
        }

        class_name = self.ui.class_comboBox_3.currentText().strip()
        date_text = self.ui.dateEdit.text().strip()

        if not class_name or not date_text:
            QMessageBox.warning(None, "هشدار", "لطفاً کلاس و تاریخ را وارد کنید.")
            return

        class_id = self._get_class_id(class_name)
        if not class_id:
            QMessageBox.critical(None, "خطا", "کلاس مورد نظر یافت نشد.")
            return

        gregorian_date = self._convert_to_gregorian(date_text)
        if not gregorian_date:
            QMessageBox.warning(None, "خطا", "تاریخ وارد شده معتبر نیست.")
            return

        students = self.student_model.get_students_by_class(class_id)
        students.sort(key=lambda s: s[2]) 
        attendance_rows = self.attendance_model.get_attendance_by_date(gregorian_date)

        # ساخت دیکشنری از رکوردهای حضور
        existing_attendance = {
            row[1]: {
                "status_hour_1": row[3],
                "status_hour_2": row[4],
                "status_hour_3": row[5],
                "status_hour_4": row[6],
                "delay_minutes": row[7]
            }
            for row in attendance_rows
        }

        self.attendance_model_view.removeRows(0, self.attendance_model_view.rowCount())

        for student in students:
            student_id, first_name, last_name = student[:3]
            attendance = existing_attendance.get(student_id, {})

            row_items = [
                QStandardItem(student_id),
                QStandardItem(first_name),
                QStandardItem(last_name),
                QStandardItem(self.status_map.get(str(attendance.get("status_hour_1", "1")), "حاضر")),
                QStandardItem(self.status_map.get(str(attendance.get("status_hour_2", "1")), "حاضر")),
                QStandardItem(self.status_map.get(str(attendance.get("status_hour_3", "1")), "حاضر")),
                QStandardItem(self.status_map.get(str(attendance.get("status_hour_4", "1")), "حاضر")),
                QStandardItem(str(attendance.get("delay_minutes", 0)))
            ]

            for i in self.non_editable_columns:
                row_items[i].setEditable(False)

            self.attendance_model_view.appendRow(row_items)

        



    def save_attendance_table(self):
        model = self.ui.attendanceTableView.model()
        row_count = model.rowCount()
        date_text = self.ui.dateEdit.text()
        gregorian_date = self._convert_to_gregorian(date_text)
        if not gregorian_date:
            QMessageBox.warning(self, "خطا", "لطفاً تاریخ را وارد کنید.")
            return

        success_count = 0
        for row in range(row_count):
            student_id = model.index(row, 0).data()
            status1 = model.index(row, 3).data()
            status2 = model.index(row, 4).data()
            status3 = model.index(row, 5).data()
            status4 = model.index(row, 6).data()
            delay = model.index(row, 7).data()

            # تبدیل به 0 یا 1

                

            s1 = self.convert_status(status1)
            s2 = self.convert_status(status2)
            s3 = self.convert_status(status3)
            s4 = self.convert_status(status4)
            delay = int(delay) if delay else 0

            # ذخیره در دیتابیس
            saved = self.attendance_model.save_attendance(
                student_id=student_id,
                date=gregorian_date,
                status_hour_1=s1,
                status_hour_2=s2,
                status_hour_3=s3,
                status_hour_4=s4,
                delay_minutes=delay
            )
            if saved:
                success_count += 1

        QMessageBox.information(None, "ذخیره", f"{success_count} رکورد با موفقیت ذخیره شد.")

    def _convert_to_gregorian(self, persian_date_str):
        try:
            parts = [int(x) for x in persian_date_str.split('-')]
            return str(JalaliDate(parts[0], parts[1], parts[2]).to_gregorian())
        except Exception as e:
            print(f"تبدیل تاریخ با خطا مواجه شد: {e}")
            return ""

    def _get_class_id(self, class_name: str):
        try:
            for cls in self.class_model.get_all_classes():
                if cls[3] == class_name:
                    return cls[0]
            return None
        except Exception as e:
            QMessageBox.critical(None, "خطا", f"خطا در دریافت اطلاعات کلاس:\n{str(e)}")
            return None
        
    def convert_status(self,text):
        if text== "حاضر":
            return 1
        elif text== "غایب":
            return 0
        else:
            return 2