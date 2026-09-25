class DialogueSummarizer:
    def __init__(self):
        self.history = []

    def add_message(self, sender: str, text: str):
        self.history.append({"sender": sender, "text": text})

    def generate_summary(self) -> dict:
        if not self.history:
            return {"total_messages": 0, "summary": "Henüz sohbet geçmişi yok."}
        
        senders = set(item["sender"] for item in self.history)
        total = len(self.history)
        
        # Create a lightweight summary of recent topics
        recent_topics = [item["text"] for item in self.history[-3:]]

        return {
            "total_messages": total,
            "unique_participants": len(senders),
            "recent_topics": recent_topics,
            "summary": f"Toplam {total} mesaj alışverişi yapıldı. Son aktif konular: {', '.join(recent_topics)}"
        }
