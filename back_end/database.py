import sqlite3

class Database:
    def __init__(self, db_file='school_attendance.db'):
        try:
            self.conn = sqlite3.connect(db_file)
            self.cursor = self.conn.cursor()
            self.create_tables()
        except sqlite3.Error as e:
            print(f"[!] Database connection failed: {e}")

    def create_tables(self):
        try:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Class (
                class_id INTEGER PRIMARY KEY AUTOINCREMENT,
                class_name TEXT NOT NULL
            )''')

            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Student (
                student_id TEXT PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                parent_phone TEXT NOT NULL,
                class_id INTEGER,
                FOREIGN KEY (class_id) REFERENCES Class(class_id)
            )''')

            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Attendance (
                attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                date TEXT NOT NULL,
                status TEXT NOT NULL,
                note TEXT,
                FOREIGN KEY (student_id) REFERENCES Student(student_id)
            )''')

            self.conn.commit()
        except sqlite3.Error as e:
            print(f"[!] Error creating tables: {e}")

    # -------------------------------
    def add_class(self, class_name):
        try:
            with self.conn:
                self.cursor.execute("INSERT INTO Class (class_name) VALUES (?)", (class_name,))
        except sqlite3.Error as e:
            print(f"[!] Error adding class: {e}")

    def get_classes(self):
        try:
            self.cursor.execute("SELECT * FROM Class")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"[!] Error fetching classes: {e}")
            return []

    # -------------------------------
    def add_student(self, student_id, first_name, last_name, parent_phone, class_id):
        try:
            with self.conn:
                self.cursor.execute('''
                    INSERT INTO Student (student_id, first_name, last_name, parent_phone, class_id)
                    VALUES (?, ?, ?, ?, ?)
                ''', (student_id, first_name, last_name, parent_phone, class_id))
        except sqlite3.IntegrityError:
            print(f"[!] Student ID '{student_id}' already exists.")
        except sqlite3.Error as e:
            print(f"[!] Error adding student: {e}")

    def get_students_by_class(self, class_id):
        try:
            self.cursor.execute("SELECT * FROM Student WHERE class_id = ?", (class_id,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"[!] Error fetching students: {e}")
            return []

    # -------------------------------
    def record_attendance(self, student_id, date, status, note=None):
        try:
            with self.conn:
                self.cursor.execute('''
                    INSERT INTO Attendance (student_id, date, status, note)
                    VALUES (?, ?, ?, ?)
                ''', (student_id, date, status, note))
        except sqlite3.IntegrityError:
            print(f"[!] Invalid student ID '{student_id}' for attendance.")
        except sqlite3.Error as e:
            print(f"[!] Error recording attendance: {e}")

    def get_attendance_for_student(self, student_id):
        try:
            self.cursor.execute("SELECT * FROM Attendance WHERE student_id = ?", (student_id,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"[!] Error fetching attendance: {e}")
            return []

    def close(self):
        self.conn.close()



if __name__ == '__main__':
    db = Database()
    db.add_class("یازدهم ریاضی")
    db.add_student("0012345678", "علی", "رضایی", "09123456789", 1)
    db.record_attendance("0012345678", "2025-07-18", "غایب", "بیمار")
    print(db.get_classes())
    print(db.get_students_by_class(1))
    print(db.get_attendance_for_student("0012345678"))
    db.close()
