from app.core.dialogue_engine import DialogueEngine

def test_dialogue_engine_learning_and_response():
    engine = DialogueEngine()

    # Test default response
    resp_default = engine.generate_response(123, "merhaba")
    assert "NOXiA 2.0" in resp_default or "Selam" in resp_default

    # Test dynamic learning
    learn_res = engine.learn_response("noksia kimdir", "NOXiA, otonom bir süper zeka operasyon merkezidir.")
    assert learn_res["status"] == "learned"

    # Test generated response for newly learned phrase
    resp_learned = engine.generate_response(123, "Noksia kimdir")
    assert "süper zeka" in resp_learned

    # Test unknown fallback
    resp_unknown = engine.generate_response(123, "kuantum bilgisayarlar")
    assert "analiz ettim" in resp_unknown
