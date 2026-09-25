import random
import sqlite3
import os

class GroupGamesManager:
    WORD_LIST = [
        {"word": "python", "hint": "A popular programming language named after a snake."},
        {"word": "telegram", "hint": "A cloud-based instant messaging platform."},
        {"word": "autonomous", "hint": "Operating independently without direct human control."},
        {"word": "algorithm", "hint": "A step-by-step procedure for solving a problem."}
    ]

    @staticmethod
    def get_db_path() -> str:
        return "noxia.db"

    @staticmethod
    def init_games_db():
        conn = sqlite3.connect(GroupGamesManager.get_db_path())
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS game_scores (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                score INTEGER DEFAULT 0
            )
        ''')
        conn.commit()
        conn.close()

    @staticmethod
    def get_random_word_puzzle() -> dict:
        item = random.choice(GroupGamesManager.WORD_LIST)
        word = item["word"]
        chars = list(word)
        random.shuffle(chars)
        scrambled = "".join(chars)
        if scrambled == word and len(word) > 1:
            random.shuffle(chars)
            scrambled = "".join(chars)

        return {
            "status": "success",
            "original": word,
            "scrambled": scrambled,
            "hint": item["hint"]
        }

    @staticmethod
    def check_puzzle_answer(user_answer: str, correct_word: str) -> bool:
        return user_answer.strip().lower() == correct_word.strip().lower()

    @staticmethod
    def add_score(user_id: int, username: str, points: int = 10) -> dict:
        GroupGamesManager.init_games_db()
        conn = sqlite3.connect(GroupGamesManager.get_db_path())
        cursor = conn.cursor()
        
        cursor.execute("SELECT score FROM game_scores WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()
        
        if row:
            new_score = row[0] + points
            cursor.execute("UPDATE game_scores SET score = ?, username = ? WHERE user_id = ?", (new_score, username, user_id))
        else:
            new_score = points
            cursor.execute("INSERT INTO game_scores (user_id, username, score) VALUES (?, ?, ?)", (user_id, username, new_score))
            
        conn.commit()
        conn.close()
        return {"status": "success", "user_id": user_id, "username": username, "total_score": new_score}

    @staticmethod
    def get_leaderboard(limit: int = 5) -> list:
        GroupGamesManager.init_games_db()
        conn = sqlite3.connect(GroupGamesManager.get_db_path())
        cursor = conn.cursor()
        cursor.execute("SELECT username, score FROM game_scores ORDER BY score DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        conn.close()
        
        return [{"username": row[0], "score": row[1]} for row in rows]
