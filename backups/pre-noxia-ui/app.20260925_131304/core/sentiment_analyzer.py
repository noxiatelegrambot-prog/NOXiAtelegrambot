class SentimentAnalyzer:
    def __init__(self):
        self.positive_words = ["harika", "süper", "mükemmel", "teşekkür", "başarılı", "iyi", "güzel"]
        self.negative_words = ["hata", "bozuk", "çalışmıyor", "sorun", "kötü", "başarısız", "yanlış"]
        self.urgent_words = ["acil", "hemen", "kritik", "alarm", "çöküş"]

    def analyze(self, text: str) -> dict:
        text_lower = text.lower()
        
        pos_count = sum(1 for w in self.positive_words if w in text_lower)
        neg_count = sum(1 for w in self.negative_words if w in text_lower)
        urg_count = sum(1 for w in self.urgent_words if w in text_lower)

        if urg_count > 0:
            tone = "urgent"
        elif pos_count > neg_count:
            tone = "positive"
        elif neg_count > pos_count:
            tone = "negative"
        else:
            tone = "neutral"

        return {
            "tone": tone,
            "scores": {
                "positive": pos_count,
                "negative": neg_count,
                "urgent": urg_count
            }
        }
