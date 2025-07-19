from database import get_connection
from models.class_model import ClassModel
from models.student_model import StudentModel
from models.attendance_model import AttendanceModel

def test_database():
    conn = get_connection()
    if not conn:
        print("Cannot connect to database.")
        return

    # ساخت جدول‌ها
    ClassModel(conn).create_table()
    StudentModel(conn).create_table()
    AttendanceModel(conn).create_table()

    # ایجاد نمونه کلاس
    class_model = ClassModel(conn)
    class_model.add_class("دهم ریاضی")

    # دریافت شناسه کلاس برای افزودن دانش آموز
    classes = class_model.get_all_classes()
    print("کلاس‌ها:", classes)
    class_id = classes[0][0] if classes else None

    # ایجاد نمونه دانش آموز
    student_model = StudentModel(conn)
    student_model.add_student("1234567890", "علی رضایی", class_id, "09121234567")

    students = student_model.get_all_students()
    print("دانش آموزان:", students)

    # ثبت حضور و غیاب
    attendance_model = AttendanceModel(conn)
    attendance_model.add_attendance("1234567890", "2025-07-18", "present", "حضور کامل")

    attendance_records = attendance_model.get_attendance_by_student("1234567890")
    print("حضور و غیاب:", attendance_records)

    conn.close()

if __name__ == "__main__":
    test_database()
