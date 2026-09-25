import re

class IntentParser:
    @staticmethod
    def parse(text: str) -> dict:
        text_lower = text.lower().strip()
        
        # Basit kural tabanlı niyet tespiti (İleride LLM ile güçlendirilecek)
        if any(kw in text_lower for kw in ["kod yaz", "script", "python", "geliştir", "pull request", "hata düzelt"]):
            intent_type = "development"
        elif any(kw in text_lower for kw in ["araştır", "bul", "nedir", "nasıl yapılır", "bak"]):
            intent_type = "research"
        elif any(kw in text_lower for kw in ["durum", "status", "görevler", "listele"]):
            intent_type = "status"
        elif any(kw in text_lower for kw in ["merhaba", "selam", "naber"]):
            intent_type = "greeting"
        else:
            intent_type = "general_chat"
            
        return {
            "intent": intent_type,
            "raw_text": text,
            "confidence": 0.95
        }
