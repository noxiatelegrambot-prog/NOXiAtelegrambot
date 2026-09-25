import sqlite3
import os

class DatabaseMemoryManager:
    def __init__(self, db_path="noxia.db"):
        self.db_path = db_path

    def init_database(self) -> bool:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS system_memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE,
                value TEXT
            )
        """)
        conn.commit()
        conn.close()
        return True

    def store_memory(self, key: str, value: str) -> bool:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO system_memory (key, value) VALUES (?, ?)", (key, value))
        conn.commit()
        conn.close()
        return True
