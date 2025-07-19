# backend/models/student_model.py

class StudentModel:
    def __init__(self, conn):
        self.conn = conn

    def create_table(self):
        try:
            with self.conn:
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS Student (
                        student_id TEXT PRIMARY KEY,  -- مثلاً کد ملی
                        full_name TEXT NOT NULL,
                        class_id INTEGER,
                        parent_phone TEXT,
                        FOREIGN KEY (class_id) REFERENCES Class(class_id)
                    )
                ''')
        except Exception as e:
            print(f"[!] Error creating Student table: {e}")

    def add_student(self, student_id, full_name, class_id, parent_phone):
        try:
            with self.conn:
                self.conn.execute('''
                    INSERT INTO Student (student_id, full_name, class_id, parent_phone)
                    VALUES (?, ?, ?, ?)
                ''', (student_id, full_name, class_id, parent_phone))
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
