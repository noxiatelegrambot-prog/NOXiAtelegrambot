import sqlite3
import random
import datetime

class SocialSuiteManager:
    @staticmethod
    def get_db_path() -> str:
        return "noxia.db"

    @staticmethod
    def init_social_db():
        conn = sqlite3.connect(SocialSuiteManager.get_db_path())
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_profiles (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                xp INTEGER DEFAULT 0,
                level INTEGER DEFAULT 1,
                streak INTEGER DEFAULT 0,
                last_active TEXT,
                badges TEXT DEFAULT "🌱 Çırak"
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS active_duels (
                duel_id TEXT PRIMARY KEY,
                player1_id INTEGER,
                player2_id INTEGER,
                word TEXT,
                status TEXT DEFAULT "WAITING"
            )
        ''')
        conn.commit()
        conn.close()

    @staticmethod
    def add_xp_and_check_level(user_id: int, username: str, xp_gain: int = 25) -> dict:
        SocialSuiteManager.init_social_db()
        conn = sqlite3.connect(SocialSuiteManager.get_db_path())
        cursor = conn.cursor()
        
        cursor.execute("SELECT xp, level, streak, badges FROM user_profiles WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()
        
        today = datetime.date.today().isoformat()
        
        if row:
            current_xp, level, streak, badges = row[0], row[1], row[2], row[3]
            new_xp = current_xp + xp_gain
            
            # Level calculation (every 100 XP = 1 Level)
            new_level = 1 + (new_xp // 100)
            
            # Badge evolution
            if new_level >= 5 and "💻 Kıdemli" not in badges:
                badges += ", 💻 Kıdemli"
            if new_level >= 10 and "👑 Prompt Kralı" not in badges:
                badges += ", 👑 Prompt Kralı"
                
            cursor.execute("""
                UPDATE user_profiles 
                SET xp = ?, level = ?, username = ?, badges = ?
                WHERE user_id = ?
            """, (new_xp, new_level, username, badges, user_id))
        else:
            new_xp = xp_gain
            new_level = 1
            streak = 1
            badges = "🌱 Çırak Kodcu"
            cursor.execute("""
                INSERT INTO user_profiles (user_id, username, xp, level, streak, last_active, badges)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (user_id, username, new_xp, new_level, streak, today, badges))
            
        conn.commit()
        conn.close()
        
        return {
            "status": "success",
            "xp": new_xp,
            "level": new_level,
            "badges": badges
        }

    @staticmethod
    def get_personality_response(event_type: str) -> str:
        responses = {
            "error": [
                "Eyvah! Kodda yine hayaletler uçuşuyor. Ben bunu hemen çözerim, sen kahveni taze tut! ☕",
                "Hata mı? O bizim için sadece küçük bir meydan okuma. 😎",
                "Fatoş sistemde: Bu hatayı yok etmek benim için çocuk oyuncağı!"
            ],
            "success": [
                "İşte bu! Sistem kaymak gibi akıyor, ellerine sağlık şampiyon! 🚀",
                "Mükemmel iş! Bu tempoyla gidersek dünyayı bile hackleriz. 🔥",
                "Harika! Kod saat gibi çalışıyor."
            ],
            "welcome": [
                "Selam! NOXiA otonom evrenine hoş geldin. Bugün hangi harikaları kodluyoruz? 🧠"
            ]
        }
        return random.choice(responses.get(event_type, ["Sistem aktif ve emrinde! ⚡"]))

    @staticmethod
    def create_duel(duel_id: str, p1_id: int, word: str) -> dict:
        SocialSuiteManager.init_social_db()
        conn = sqlite3.connect(SocialSuiteManager.get_db_path())
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO active_duels (duel_id, player1_id, word, status)
            VALUES (?, ?, ?, 'WAITING')
        """, (duel_id, p1_id, word))
        conn.commit()
        conn.close()
        return {"status": "success", "duel_id": duel_id, "word": word}
