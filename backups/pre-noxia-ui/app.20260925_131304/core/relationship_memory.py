class RelationshipMemoryEngine:
    def __init__(self):
        self.memory_store = {}

    def store_fact(self, user_id: str, key: str, value: str) -> bool:
        if user_id not in self.memory_store:
            self.memory_store[user_id] = {}
        self.memory_store[user_id][key] = value
        return True

    def recall_fact(self, user_id: str, key: str) -> str:
        if user_id in self.memory_store and key in self.memory_store[user_id]:
            return self.memory_store[user_id][key]
        return None

    def get_user_profile_summary(self, user_id: str) -> dict:
        facts = self.memory_store.get(user_id, {})
        return {
            "user_id": user_id,
            "stored_facts_count": len(facts),
            "facts": facts
        }
