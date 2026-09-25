import re


class IntentTransmuter:
    CHAT_PATTERNS = (
        r"^(naber|ne haber)$",
        r"^(nasılsın|nasilsin)$",
        r"^(merhaba|selam|sa|selamlar)$",
        r"^(günaydın|gunaydin)$",
        r"^(iyi akşamlar|iyi aksamlar)$",
        r"^(iyi geceler)$",
        r"^(teşekkürler|tesekkurler|teşekkür ederim|tesekkur ederim)$",
        r"^(sağ ol|sag ol)$",
        r"^(eyvallah)$",
        r"^(görüşürüz|gorusuruz|bye|hoşça kal|hosca kal)$",
    )

    LEARN_PREFIXES = (
        "öğren:",
        "ogren:",
        "öğret:",
        "ogret:",
        "learn:",
    )

    TASK_HINTS = (
        "yap", "oluştur", "olustur", "düzelt", "duzelt",
        "değiştir", "degistir", "güncelle", "guncelle",
        "ekle", "sil", "kur", "yükle", "yukle", "deploy",
        "test et", "kontrol et", "analiz et", "araştır",
        "arastir", "kodla", "çalıştır", "calistir", "incele",
        "uygula",
    )

    def __init__(self):
        self.transmutation_rules = {
            "durum": {
                "action": "fetch_telemetry_snapshot",
                "target": "system",
            },
            "temizle": {
                "action": "optimize_memory_cache",
                "target": "memory",
            },
            "güvenlik": {
                "action": "inspect_firewall_logs",
                "target": "security",
            },
        }

    @staticmethod
    def _normalize(text: str) -> str:
        text = text.lower().strip()
        return re.sub(r"\s+", " ", text)

    def transmute(self, user_command: str) -> dict:
        text = self._normalize(user_command)

        if not text:
            return {
                "intent": "unknown",
                "transmuted_action": "ignore",
                "target_subsystem": "none",
                "confidence": 1.0,
            }

        if text.startswith(self.LEARN_PREFIXES):
            return {
                "intent": "learn",
                "transmuted_action": "learn_dialogue",
                "target_subsystem": "learning_engine",
                "confidence": 1.0,
            }

        if any(re.match(pattern, text) for pattern in self.CHAT_PATTERNS):
            return {
                "intent": "chat",
                "transmuted_action": "generate_dialogue_response",
                "target_subsystem": "dialogue_engine",
                "confidence": 1.0,
            }

        for keyword, rule in self.transmutation_rules.items():
            if keyword in text:
                return {
                    "intent": "task",
                    "transmuted_action": rule["action"],
                    "target_subsystem": rule["target"],
                    "confidence": 0.9,
                }

        if any(hint in text for hint in self.TASK_HINTS):
            return {
                "intent": "task",
                "transmuted_action": "execute_standard_task",
                "target_subsystem": "orchestrator",
                "confidence": 0.8,
            }

        return {
            "intent": "chat",
            "transmuted_action": "generate_dialogue_response",
            "target_subsystem": "dialogue_engine",
            "confidence": 0.55,
        }
