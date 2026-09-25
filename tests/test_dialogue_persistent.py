from app.core.dialogue_persistent import PersistentDialogueEngine

def test_persistent_dialogue():
    engine = PersistentDialogueEngine()
    
    res = engine.learn_persistent("ankara trafik", "Ankara'da metro ve otobüs hatları aktif olarak çalışıyor.")
    assert res["status"] == "persisted"

    reply = engine.get_response("Ankara trafik durumu nasıl?")
    assert "metro ve otobüs" in reply
