# back_end/models/student_model.py
from back_end.database import get_connection

class StudentModel:
    def __init__(self):
        self.conn = get_connection()
        self.create_table()

    def create_table(self):
        try:
            with self.conn:
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS Student (
                        student_id TEXT PRIMARY KEY,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        father_name TEXT NOT NULL,
                        class_id INTEGER,
                        parent_phone TEXT,
                        FOREIGN KEY (class_id) REFERENCES Class(class_id)
                    )
                ''')
        except Exception as e:
            print(f"[!] Error creating Student table: {e}")

    def add_student(self, student_id, first_name, last_name, father_name, class_id, parent_phone):
        try:
            with self.conn:
                self.conn.execute('''
                    INSERT INTO Student (student_id, first_name, last_name, father_name, class_id, parent_phone)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (student_id, first_name, last_name, father_name, class_id, parent_phone))
        except Exception as e:
            print(f"[!] Error adding student: {e}")

    def get_all_students(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Student")
            return cursor.fetchall()
        except Exception as e:
            print(f"[!] Error fetching students: {e}")
            return []

    def __del__(self):
        if self.conn:
            self.conn.close()
