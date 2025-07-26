from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox
from PySide6.QtCore import Qt
import sys

class RightAlignedComboBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Right-to-Left ComboBox")

        # ساختن ComboBox
        self.combo = QComboBox()
        self.combo.addItems(["فارسی", "عربی", "انگلیسی", "فرانسه"])

        # تنظیم راست‌چین بودن
        self.combo.setLayoutDirection(Qt.RightToLeft)
        self.combo.setEditable(True)
        self.combo.lineEdit().setAlignment(Qt.AlignRight)
        self.combo.setEditable(False)

        # چیدمان ساده
        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RightAlignedComboBoxDemo()
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec())
