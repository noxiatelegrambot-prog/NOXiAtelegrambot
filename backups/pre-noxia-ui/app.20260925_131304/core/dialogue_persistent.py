import sqlite3
import os

class PersistentDialogueEngine:
    def __init__(self, db_path="noxia.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS learned_dialogues (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    trigger TEXT UNIQUE,
                    response TEXT
                )
            """)
            conn.commit()

    def learn_persistent(self, trigger: str, response: str) -> dict:
        key = trigger.lower().strip()
        ans = response.strip()
        with sqlite3.connect(self.db_path) as conn:
            try:
                conn.execute(
                    "INSERT OR REPLACE INTO learned_dialogues (trigger, response) VALUES (?, ?)",
                    (key, ans)
                )
                conn.commit()
                return {"status": "persisted", "trigger": key, "response": ans}
            except Exception as e:
                return {"status": "error", "reason": str(e)}

    def get_response(self, message: str) -> str:
        msg_clean = message.lower().strip()
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            # Exact or partial match check in db
            cursor.execute("SELECT trigger, response FROM learned_dialogues")
            rows = cursor.fetchall()
            
            for trigger, response in rows:
                if trigger in msg_clean:
                    return response

        return f"Kalıcı hafızada '{message}' için eşleşme bulunamadı."
