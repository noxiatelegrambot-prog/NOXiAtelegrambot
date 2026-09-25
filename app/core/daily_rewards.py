import sqlite3
import datetime
from app.core.social_suite import SocialSuiteManager

class DailyRewardsManager:
    @staticmethod
    def claim_daily_bonus(user_id: int, username: str) -> dict:
        SocialSuiteManager.init_social_db()
        conn = sqlite3.connect(SocialSuiteManager.get_db_path())
        cursor = conn.cursor()
        
        cursor.execute("SELECT streak, last_active, xp FROM user_profiles WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()
        
        today = datetime.date.today().isoformat()
        yesterday = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
        
        if row:
            streak, last_active, current_xp = row[0], row[1], row[2]
            if last_active == today:
                return {
                    "status": "already_claimed",
                    "message": "Bugünkü günlük ödülünü zaten aldın! Yarın tekrar uğra şampiyon. ⏳"
                }
            elif last_active == yesterday:
                streak += 1
            else:
                streak = 1 # Streak broken
        else:
            streak = 1
            
        # Base reward + streak bonus
        reward_xp = 50 + (streak * 10)
        
        # Update profile using SocialSuite manager logic or direct update
        SocialSuiteManager.add_xp_and_check_level(user_id, username, reward_xp)
        
        cursor.execute("""
            UPDATE user_profiles 
            SET streak = ?, last_active = ?
            WHERE user_id = ?
        """, (streak, today, user_id))
        conn.commit()
        conn.close()
        
        return {
            "status": "success",
            "streak": streak,
            "reward_xp": reward_xp,
            "message": f"🎉 Günlük ödülün alındı! +{reward_xp} XP kazandın (Seri: {streak} gün 🔥)."
        }
