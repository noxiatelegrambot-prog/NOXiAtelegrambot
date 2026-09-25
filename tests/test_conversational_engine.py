from app.core.conversational_engine import ConversationalEngine

def test_conversational_response():
    res = ConversationalEngine.process_chat_message("Merhaba NOXiA, sistem nasıl gidiyor?", {"persona": "technical_mentor"})
    assert res["status"] == "success"
    assert res["persona_applied"] == "technical_mentor"
    assert "mesajını aldım" in res["response"]

def test_sentiment_detection():
    pos_res = ConversationalEngine.process_chat_message("Harika bir iş çıkardın teşekkürler!")
    assert pos_res["sentiment"] == "positive"

    neg_res = ConversationalEngine.process_chat_message("Kod çalışmıyor hata veriyor.")
    assert neg_res["sentiment"] == "frustrated"

def test_persona_adjustment():
    assert ConversationalEngine.adjust_persona("dark_aesthetic") is True
    assert ConversationalEngine.adjust_persona("invalid_persona") is False
