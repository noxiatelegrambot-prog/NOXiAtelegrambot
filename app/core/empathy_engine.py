class EmpathyEngine:
    def __init__(self):
        self.user_moods = {}

    def update_mood(self, user_id: str, sentiment: str) -> str:
        # Track mood history and compute empathetic response strategy
        if user_id not in self.user_moods:
            self.user_moods[user_id] = []
        self.user_moods[user_id].append(sentiment)
        
        # Keep last 10 moods
        if len(self.user_moods[user_id]) > 10:
            self.user_moods[user_id] = self.user_moods[user_id][-10:]
            
        recent_moods = self.user_moods[user_id]
        if recent_moods.count("frustrated") >= 2:
            return "supportive_and_calming"
        elif sentiment == "positive":
            return "enthusiastic_and_engaging"
        return "balanced_and_attentive"
