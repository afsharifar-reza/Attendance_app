# backend/database.py

import sqlite3

def get_connection(db_name="school_attendance.db"):
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(f"[!] Database connection error: {e}")
        return None
