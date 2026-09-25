from app.core.planner import Planner

def test_planner_intent_classification():
    res1 = Planner.classify_intent("Lütfen yeni bir python modülü yaz ve kodla")
    assert res1["intent"] == "coding"

    res2 = Planner.classify_intent("Ankara'daki tarihi yerleri araştır")
    assert res2["intent"] == "research"

    res3 = Planner.classify_intent("Sistem testlerini çalıştır")
    assert res3["intent"] == "testing"
