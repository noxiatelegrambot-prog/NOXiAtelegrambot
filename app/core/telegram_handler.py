class TelegramMessageHandler:
    def __init__(self, conversational_engine, memory_manager, empathy_engine, tone_engine):
        self.conversational_engine = conversational_engine
        self.memory_manager = memory_manager
        self.empathy_engine = empathy_engine
        self.tone_engine = tone_engine

    def handle_incoming_message(self, user_id: str, message_text: str, persona: str = "sharp_and_intelligent", is_group: bool = False, bot_username: str = "@noxia_bot") -> dict:
        # Check if bot should respond in group (e.g. mentioned or direct chat)
        if is_group and bot_username not in message_text and "noxia" not in message_text.lower():
            return {"status": "ignored", "reason": "Not addressed to bot in group chat"}

        # 1. Record user turn in memory
        self.memory_manager.add_turn(user_id, "user", message_text)

        # 2. Process through conversational engine
        chat_res = self.conversational_engine.process_chat_message(message_text, {"persona": persona})
        sentiment = chat_res.get("sentiment", "neutral")

        # 3. Evaluate mood and empathy strategy
        empathy_strategy = self.empathy_engine.update_mood(user_id, sentiment)

        # 4. Apply persona tone
        raw_response = chat_res.get("response", "Seni dinliyorum.")
        final_response = self.tone_engine.apply_tone(raw_response, persona)

        # 5. Record assistant turn in memory
        self.memory_manager.add_turn(user_id, "assistant", final_response)

        return {
            "status": "success",
            "sentiment": sentiment,
            "empathy_strategy": empathy_strategy,
            "response": final_response
        }
