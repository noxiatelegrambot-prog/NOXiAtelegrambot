class Planner:
    @staticmethod
    def classify_intent(user_input: str) -> dict:
        text = user_input.lower()
        intent = "general"
        if any(w in text for w in ["araştır", "bul", "search", "nedir"]):
            intent = "research"
        elif any(w in text for w in ["yaz", "kod", "geliştir", "code", "refactor"]):
            intent = "coding"
        elif any(w in text for w in ["test", "kontrol", "verify"]):
            intent = "testing"
        elif any(w in text for w in ["deploy", "yükle", "release"]):
            intent = "deployment"

        return {
            "status": "success",
            "intent": intent,
            "complexity": "medium" if len(text) > 20 else "low",
            "requires_decomposition": len(text) > 40
        }
