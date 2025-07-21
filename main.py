from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox
from PySide6.QtGui import QPixmap
from front_end.ui.ui_first import Ui_MainWindow  # توجه کن که این مسیر هم باید با نام پوشه درست باشد
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pic_main.setPixmap(QPixmap("front_end/picture/logo.png"))

        self.ui.login_btn.clicked.connect(self.show_login_message)
        self.ui.reg_btn.clicked.connect(self.show_register_message)
    def show_login_message(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("ورود")
        msg_box.setText("کلیک کردید :)")
        msg_box.setIcon(QMessageBox.Information)  # آیکون اطلاعات
        msg_box.exec()
    def show_register_message(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("ثبت‌نام")
        msg_box.setText("ثبت‌نام کلیک شد :)")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec()    

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
