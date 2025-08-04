from back_end.database import get_connection

class AttendanceModel:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        try:
            with self.conn:
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS Attendance (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id TEXT NOT NULL,
                        date TEXT NOT NULL,
                        status_hour_1 INTEGER DEFAULT 0,
                        status_hour_2 INTEGER DEFAULT 0,
                        status_hour_3 INTEGER DEFAULT 0,
                        status_hour_4 INTEGER DEFAULT 0,
                        delay_minutes INTEGER DEFAULT 0,
                        FOREIGN KEY (student_id) REFERENCES Student(student_id),
                        UNIQUE(student_id, date)
                    )
                ''')
        except Exception as e:
            print(f"[!] خطا در ساخت جدول Attendance: {e}")

    def get_attendance_record(self, student_id, date):
        try:
            with self.conn:
                self.cursor.execute('''
                    SELECT id FROM Attendance
                    WHERE student_id = ? AND date = ?
                ''', (student_id, date))
                return self.cursor.fetchone()
        except Exception as e:
            print(f"[!] خطا در بررسی رکورد موجود: {e}")
            return None

    def save_attendance(self, student_id, date,
                        status_hour_1=0, status_hour_2=0,
                        status_hour_3=0, status_hour_4=0,
                        delay_minutes=0):
        try:
            existing = self.get_attendance_record(student_id, date)
            with self.conn:
                if existing:
                    attendance_id = existing[0]
                    self.conn.execute('''
                        UPDATE Attendance SET
                            status_hour_1 = ?, status_hour_2 = ?,
                            status_hour_3 = ?, status_hour_4 = ?,
                            delay_minutes = ?
                        WHERE id = ?
                    ''', (status_hour_1, status_hour_2, status_hour_3, status_hour_4, delay_minutes, attendance_id))
                else:
                    self.conn.execute('''
                        INSERT INTO Attendance (
                            student_id, date,
                            status_hour_1, status_hour_2,
                            status_hour_3, status_hour_4,
                            delay_minutes
                        ) VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (student_id, date, status_hour_1, status_hour_2, status_hour_3, status_hour_4, delay_minutes))
            return True
        except Exception as e:
            print(f"[!] خطا در ذخیره حضور و غیاب: {e}")
            return False

    def get_attendance_by_date(self, date):
        try:
            with self.conn:
                self.cursor.execute('SELECT * FROM Attendance WHERE date = ?', (date,))
                return self.cursor.fetchall()
        except Exception as e:
            print(f"[!] خطا در دریافت داده‌های روز {date}: {e}")
            return []

    def get_attendance_by_student(self, student_id):
        try:
            with self.conn:
                self.cursor.execute('SELECT * FROM Attendance WHERE student_id = ?', (student_id,))
                return self.cursor.fetchall()
        except Exception as e:
            print(f"[!] خطا در دریافت حضور و غیاب دانش‌آموز: {e}")
            return []

    def get_attendance_report_by_class(self, class_id, start_date, end_date):
        try:
            with self.conn:
                query = """
                    SELECT
                        s.student_id,
                        s.first_name,
                        s.last_name,
                        a.date,
                        a.status_hour_1,
                        a.status_hour_2,
                        a.status_hour_3,
                        a.status_hour_4,
                        a.delay_minutes
                    FROM attendance a
                    JOIN student s ON a.student_id = s.student_id
                    WHERE s.class_id = ?
                    AND a.date BETWEEN ? AND ?
                    ORDER BY a.date
                """
                self.cursor.execute(query, (class_id, start_date, end_date))
                return self.cursor.fetchall()
        except Exception as e:
            print(f"[!] خطا در دریافت گزارش کلاس: {e}")
            return []

    def get_attendance_report_by_student(self, student_id, start_date, end_date):
        try:
            with self.conn:
                query = """
                    SELECT
                        a.date,
                        a.status_hour_1,
                        a.status_hour_2,
                        a.status_hour_3,
                        a.status_hour_4,
                        a.delay_minutes
                    FROM attendance a
                    WHERE a.student_id = ?
                    AND a.date BETWEEN ? AND ?
                    ORDER BY a.date
                """
                self.cursor.execute(query, (student_id, start_date, end_date))
                return self.cursor.fetchall()
        except Exception as e:
            print(f"[!] خطا در دریافت گزارش دانش‌آموز: {e}")
            return []

    def __del__(self):
        if self.conn:
            self.conn.close()
