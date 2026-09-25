class AdaptiveLearningEngine:
    def __init__(self):
        self.knowledge_weights = {}

    def register_pattern(self, pattern: str, initial_weight: float = 1.0):
        self.knowledge_weights[pattern.lower().strip()] = initial_weight

    def apply_feedback(self, pattern: str, is_positive: bool) -> dict:
        key = pattern.lower().strip()
        if key not in self.knowledge_weights:
            self.knowledge_weights[key] = 1.0

        adjustment = 0.2 if is_positive else -0.3
        new_weight = max(0.1, self.knowledge_weights[key] + adjustment)
        self.knowledge_weights[key] = round(new_weight, 2)

        return {
            "pattern": key,
            "feedback": "positive" if is_positive else "negative",
            "updated_weight": self.knowledge_weights[key],
            "status": "adapted"
        }

    def get_weight(self, pattern: str) -> float:
        return self.knowledge_weights.get(pattern.lower().strip(), 1.0)
