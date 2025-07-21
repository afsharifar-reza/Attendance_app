from PySide6.QtWidgets import QMainWindow,QMessageBox,QTableWidgetItem
from PySide6.QtWidgets import QWidget


class ManageTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.manage_tab = self.parent.ui.manage_tab