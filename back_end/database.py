# back_end/database.py

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "school_attendance.db")

def get_connection():
    try:
        return sqlite3.connect(DB_PATH)
    except sqlite3.Error as e:
        print(f"[!] Database connection error: {e}")
        return None
