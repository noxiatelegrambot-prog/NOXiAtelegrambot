class ToneEngine:
    @staticmethod
    def apply_tone(message: str, persona: str) -> str:
        # Apply stylistic and tonal modifications based on active persona
        if persona == "dark_aesthetic":
            return f"~ {message} ...gölgelerin ötesinden."
        elif persona == "technical_mentor":
            return f"[Mentor Log]: {message} — Kod kalitesi her şeydir."
        elif persona == "empathetic_friend":
            return f"Canım benim, {message} Yanındayım."
        return f"{message}"
