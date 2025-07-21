from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from back_end.models.class_model import ClassModel

class ClassManager:
    def __init__(self, ui, connection):
        self.ui = ui
        try:
            self.model = ClassModel(connection)
        except ConnectionError as e:
            QMessageBox.critical(None, "Database Error", str(e))
            raise

    def add_new_class(self):  # نام یکسان با dashboard.py
        grade = self.ui.Grade_comboBox.currentText().strip()
        field = self.ui.Field_comboBox.currentText().strip()

        if not (grade and field):
            QMessageBox.warning(None, "خطا", "لطفاً پایه و رشته را انتخاب کنید")
            return False

        success = self.model.add_class(grade, field)
        if success:
            self.load_classes()
            QMessageBox.information(None, "موفقیت", "کلاس با موفقیت ثبت شد")
            return True
        else:
            QMessageBox.warning(None, "خطا", "کلاس تکراری است")
            return False

    def load_classes(self):  # نام یکسان با dashboard.py
        classes = self.model.get_all_classes()
        table = self.ui.class_tableWidget
        table.setRowCount(len(classes))
        
        for row, (class_id, grade, field) in enumerate(classes):
            table.setItem(row, 0, QTableWidgetItem(str(class_id)))
            table.setItem(row, 1, QTableWidgetItem(grade))
            table.setItem(row, 2, QTableWidgetItem(field))