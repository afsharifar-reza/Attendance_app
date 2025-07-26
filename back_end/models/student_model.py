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
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO Student (student_id, first_name, last_name, father_name, class_id, parent_phone)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (student_id, first_name, last_name, father_name, class_id, parent_phone))
            self.conn.commit()
            return cursor.rowcount > 0  # اگر سطری درج شده باشد، True برمی‌گردد
        except Exception as e:
            print(f"خطا در add_student: {e}")
            return False
        

    def update_student(self, student_id, first_name, last_name, father_name, class_id, parent_phone):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE Student
                SET first_name = ?, last_name = ?, father_name = ?, class_id = ?, parent_phone = ?
                WHERE student_id = ?
            """, (first_name, last_name, father_name, class_id, parent_phone, student_id))
            self.conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"خطا در update_student: {e}")
            return False


    def get_all_students(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Student")
            return cursor.fetchall()
        except Exception as e:
            print(f"[!] Error fetching students: {e}")
            return []
    def search_students(self, first_name=None, last_name=None, student_id=None):
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM Student WHERE 1=1"
            params = []

            if first_name:
                query += " AND first_name LIKE ?"
                params.append(f"%{first_name}%")

            if last_name:
                query += " AND last_name LIKE ?"
                params.append(f"%{last_name}%")

            if student_id:
                query += " AND student_id LIKE ?"
                params.append(f"%{student_id}%")

            cursor.execute(query, params)
            return cursor.fetchall()
        except Exception as e:
            print(f"[!] Error searching students: {e}")
            return []
        
    def get_students_by_class(self, class_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Student WHERE class_id = ?", (class_id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"[!] Error in get_students_by_class: {e}")
            return []


    def __del__(self):
        if self.conn:
            self.conn.close()
