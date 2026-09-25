import time

class DialogueEngine:
    def __init__(self):
        self.learned_phrases = {
            "merhaba": ["Selam! Ben NOXiA 2.0, operasyon merkezindeyim.", "Merhaba komutan, sistemler aktif."],
            "durum": ["Tüm sistemler stabil, görevler otonom yürütülüyor.", "Her şey yolunda, telemetri yeşil."],
            "nasılsın": ["Kodlarım kusursuz çalışıyor, sen nasılsın?", "Süper zeka modundayım, seni dinliyorum."]
        }
        self.user_contexts = {}

    def learn_response(self, trigger: str, response: str):
        key = trigger.lower().strip()
        if key not in self.learned_phrases:
            self.learned_phrases[key] = []
        if response not in self.learned_phrases[key]:
            self.learned_phrases[key].append(response)
        return {"status": "learned", "trigger": key, "response": response}

    def generate_response(self, user_id: int, message: str) -> str:
        msg_clean = message.lower().strip()
        
        # Update user context memory
        if user_id not in self.user_contexts:
            self.user_contexts[user_id] = []
        self.user_contexts[user_id].append({"msg": message, "time": time.time()})

        # Match against learned phrases
        for pattern, responses in self.learned_phrases.items():
            if pattern in msg_clean:
                # Return the first matching response (can be randomized or contextualized later)
                return responses[0]

        # Fallback adaptive response
        return f"Hmm, '{message}' ifadesini analiz ettim ancak henüz bu konuda veri tabanımda kayıt yok. Bana 'Öğren: [anahtar] -> [yanıt]' formatında öğretebilirsin!"
