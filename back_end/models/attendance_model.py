# backend/models/attendance_model.py

class AttendanceModel:
    def __init__(self, conn):
        self.conn = conn

    def create_table(self):
        try:
            with self.conn:
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS Attendance (
                        attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id TEXT,
                        date TEXT,
                        status TEXT,  -- مثلا 'present', 'absent', 'late'
                        note TEXT,
                        FOREIGN KEY (student_id) REFERENCES Student(student_id)
                    )
                ''')
        except Exception as e:
            print(f"[!] Error creating Attendance table: {e}")

    def add_attendance(self, student_id, date, status, note=None):
        try:
            with self.conn:
                self.conn.execute('''
                    INSERT INTO Attendance (student_id, date, status, note)
                    VALUES (?, ?, ?, ?)
                ''', (student_id, date, status, note))
        except Exception as e:
            print(f"[!] Error adding attendance: {e}")

    def get_attendance_by_student(self, student_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Attendance WHERE student_id = ?", (student_id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"[!] Error fetching attendance: {e}")
            return []
