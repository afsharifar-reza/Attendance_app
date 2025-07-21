import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from back_end.database import get_connection

class ClassModel:
    def __init__(self):
        self.conn = get_connection()
        self.create_table()

    def create_table(self):
        try:
            with self.conn:
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS Class (
                        class_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        grade TEXT NOT NULL,
                        field TEXT NOT NULL,
                        class_name TEXT NOT NULL,
                        UNIQUE(grade, field)
                    )
                ''')
        except Exception as e:
            print(f"[!] Error creating Class table: {e}")

    def add_class(self, grade, field):
        try:
            if self.class_exists(grade, field):
                print("[!] Class already exists. Skipping insert.")
                return None

            class_name = f"{grade} {field}"
            with self.conn:
                cursor = self.conn.execute(
                    "INSERT INTO Class (grade, field, class_name) VALUES (?, ?, ?)",
                    (grade, field, class_name)
                )
                return cursor.lastrowid
        except Exception as e:
            print(f"[!] Error adding class: {e}")
            return None

    def get_all_classes(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Class")
            return cursor.fetchall()
        except Exception as e:
            print(f"[!] Error fetching classes: {e}")
            return []

    def class_exists(self, grade, field):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT class_id FROM Class WHERE grade = ? AND field = ?",
                (grade, field)
            )
            return cursor.fetchone() is not None
        except Exception as e:
            print(f"[!] Error checking class existence: {e}")
            return False

    def __del__(self):
        if self.conn:
            self.conn.close()
