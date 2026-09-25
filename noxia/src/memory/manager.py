from src.database.models import db_session

class MemoryManager:
    @staticmethod
    def save_memory(user_id: int, context_type: str, content: str, importance: float = 1.0):
        with db_session() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO memories (user_id, context_type, content, importance) VALUES (?, ?, ?, ?)",
                (user_id, context_type, content, importance)
            )

    @staticmethod
    def get_user_memories(user_id: int, limit: int = 5):
        with db_session() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT context_type, content FROM memories WHERE user_id = ? ORDER BY created_at DESC LIMIT ?",
                (user_id, limit)
            )
            return [dict(row) for row in cursor.fetchall()]
