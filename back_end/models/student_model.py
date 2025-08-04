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
                self.conn.execute("""
                    INSERT INTO Student (student_id, first_name, last_name, father_name, class_id, parent_phone)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (student_id, first_name, last_name, father_name, class_id, parent_phone))
            return True
        except Exception as e:
            print(f"[!] Error in add_student: {e}")
            return False

    def update_student(self, student_id, first_name, last_name, father_name, class_id, parent_phone):
        try:
            with self.conn:
                result = self.conn.execute("""
                    UPDATE Student
                    SET first_name = ?, last_name = ?, father_name = ?, class_id = ?, parent_phone = ?
                    WHERE student_id = ?
                """, (first_name, last_name, father_name, class_id, parent_phone, student_id))
            return result.rowcount > 0
        except Exception as e:
            print(f"[!] Error in update_student: {e}")
            return False

    def get_all_students(self):
        try:
            with self.conn:
                cursor = self.conn.execute("SELECT * FROM Student")
                return cursor.fetchall()
        except Exception as e:
            print(f"[!] Error fetching students: {e}")
            return []

    def search_students(self, first_name=None, last_name=None, student_id=None):
        try:
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

            with self.conn:
                cursor = self.conn.execute(query, params)
                return cursor.fetchall()
        except Exception as e:
            print(f"[!] Error searching students: {e}")
            return []

    def get_students_by_class(self, class_id):
        try:
            with self.conn:
                cursor = self.conn.execute("SELECT * FROM Student WHERE class_id = ?", (class_id,))
                return cursor.fetchall()
        except Exception as e:
            print(f"[!] Error in get_students_by_class: {e}")
            return []

    def search_students_with_classname(self, first_name=None, last_name=None, student_id=None):
        try:
            query = """
                SELECT Student.student_id, Student.first_name, Student.last_name,
                       Student.father_name, Class.class_name, Student.parent_phone
                FROM Student
                LEFT JOIN Class ON Student.class_id = Class.class_id
                WHERE 1=1
            """
            params = []

            if first_name:
                query += " AND Student.first_name LIKE ?"
                params.append(f"%{first_name}%")
            if last_name:
                query += " AND Student.last_name LIKE ?"
                params.append(f"%{last_name}%")
            if student_id:
                query += " AND Student.student_id LIKE ?"
                params.append(f"%{student_id}%")

            with self.conn:
                cursor = self.conn.execute(query, params)
                return cursor.fetchall()
        except Exception as e:
            print(f"[!] Error searching students with class name: {e}")
            return []

    def __del__(self):
        if self.conn:
            self.conn.close()
