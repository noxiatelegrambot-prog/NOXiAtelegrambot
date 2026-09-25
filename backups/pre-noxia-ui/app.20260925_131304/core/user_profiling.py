class UserProfilingEngine:
    def __init__(self):
        self.profiles = {}

    def record_interaction(self, user_id: int, action_type: str):
        if user_id not in self.profiles:
            self.profiles[user_id] = {
                "total_interactions": 0,
                "actions": {}
            }
        
        self.profiles[user_id]["total_interactions"] += 1
        action_counts = self.profiles[user_id]["actions"]
        action_counts[action_type] = action_counts.get(action_type, 0) + 1

    def get_user_profile(self, user_id: int) -> dict:
        if user_id not in self.profiles:
            return {"total_interactions": 0, "favorite_action": None, "actions": {}}
        
        data = self.profiles[user_id]
        fav_action = max(data["actions"], key=data["actions"].get) if data["actions"] else None
        
        return {
            "total_interactions": data["total_interactions"],
            "favorite_action": fav_action,
            "actions": data["actions"]
        }
