from app.core.tone_engine import ToneEngine

def test_dark_aesthetic_tone():
    styled = ToneEngine.apply_tone("Sistem çalışıyor", "dark_aesthetic")
    assert "~" in styled
    assert "gölgelerin ötesinden" in styled

def test_technical_mentor_tone():
    styled = ToneEngine.apply_tone("Testler başarılı", "technical_mentor")
    assert "[Mentor Log]" in styled
    assert "Kod kalitesi" in styled

def test_empathetic_friend_tone():
    styled = ToneEngine.apply_tone("Her şeyi çözeriz", "empathetic_friend")
    assert "Yanındayım" in styled
