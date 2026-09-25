class ConversationalMemoryManager:
    def __init__(self):
        self.sessions = {}

    def add_turn(self, user_id: str, role: str, content: str) -> bool:
        if user_id not in self.sessions:
            self.sessions[user_id] = []
        self.sessions[user_id].append({"role": role, "content": content})
        # Keep window manageable (last 20 turns)
        if len(self.sessions[user_id]) > 20:
            self.sessions[user_id] = self.sessions[user_id][-20:]
        return True

    def get_history(self, user_id: str) -> list:
        return self.sessions.get(user_id, [])

    def clear_history(self, user_id: str) -> bool:
        if user_id in self.sessions:
            self.sessions[user_id] = []
            return True
        return False
