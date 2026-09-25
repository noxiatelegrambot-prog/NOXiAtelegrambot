from app.core.telegram_handler import TelegramMessageHandler
from app.core.conversational_engine import ConversationalEngine
from app.core.conversational_memory import ConversationalMemoryManager
from app.core.empathy_engine import EmpathyEngine
from app.core.tone_engine import ToneEngine

def test_telegram_handler_direct_message():
    handler = TelegramMessageHandler(
        ConversationalEngine(),
        ConversationalMemoryManager(),
        EmpathyEngine(),
        ToneEngine()
    )

    res = handler.handle_incoming_message("user_tg_1", "Harika bir bot olmuş ellerine sağlık", persona="dark_aesthetic", is_group=False)
    assert res["status"] == "success"
    assert res["sentiment"] == "positive"
    assert "~" in res["response"]

def test_telegram_handler_group_ignored():
    handler = TelegramMessageHandler(
        ConversationalEngine(),
        ConversationalMemoryManager(),
        EmpathyEngine(),
        ToneEngine()
    )

    res = handler.handle_incoming_message("user_tg_2", "Arkadaşlar bugün hava çok güzel", persona="technical_mentor", is_group=True, bot_username="@noxia_bot")
    assert res["status"] == "ignored"
