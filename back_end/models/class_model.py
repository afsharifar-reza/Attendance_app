# backend/models/class_model.py

class ClassModel:
    def __init__(self, conn):
        self.conn = conn

    def create_table(self):
        try:
            with self.conn:
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS Class (
                        class_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        class_name TEXT NOT NULL
                    )
                ''')
        except Exception as e:
            print(f"[!] Error creating Class table: {e}")

    def add_class(self, class_name):
        try:
            with self.conn:
                self.conn.execute("INSERT INTO Class (class_name) VALUES (?)", (class_name,))
        except Exception as e:
            print(f"[!] Error adding class: {e}")

    def get_all_classes(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Class")
            return cursor.fetchall()
        except Exception as e:
            print(f"[!] Error fetching classes: {e}")
            return []
