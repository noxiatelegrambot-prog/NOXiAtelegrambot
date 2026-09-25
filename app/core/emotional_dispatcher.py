from app.core.sentiment_analyzer import SentimentAnalyzer
from app.core.dialogue_persistent import PersistentDialogueEngine

class EmotionalDispatcher:
    def __init__(self):
        self.sentiment = SentimentAnalyzer()
        self.dialogue = PersistentDialogueEngine()

    def process_message(self, user_id: int, message: str) -> dict:
        analysis = self.sentiment.analyze(message)
        tone = analysis["tone"]

        # Determine automated action based on tone
        triggered_action = None
        if tone == "urgent":
            triggered_action = "initiate_emergency_health_check"
        elif tone == "negative":
            triggered_action = "log_error_pattern"
        else:
            triggered_action = "standard_dialogue_response"

        # Get response from persistent dialogue engine or generate contextual reply
        base_response = self.dialogue.get_response(message)

        return {
            "tone": tone,
            "scores": analysis["scores"],
            "action": triggered_action,
            "response": base_response
        }
