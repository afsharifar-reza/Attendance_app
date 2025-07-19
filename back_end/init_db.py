# init_db.py

from database import get_connection
from models.class_model import ClassModel
from models.student_model import StudentModel
from models.attendance_model import AttendanceModel

def initialize_database():
    conn = get_connection()
    if conn:
        ClassModel(conn).create_table()
        StudentModel(conn).create_table()
        AttendanceModel(conn).create_table()
        conn.close()
        print("All tables created successfully.")
    else:
        print("Failed to connect to database.")

if __name__ == "__main__":
    initialize_database()