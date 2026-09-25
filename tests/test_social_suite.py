from app.core.social_suite import SocialSuiteManager

def test_xp_and_leveling():
    SocialSuiteManager.init_social_db()
    res = SocialSuiteManager.add_xp_and_check_level(12345, "grup_Uyesi", 150)
    assert res["status"] == "success"
    assert res["xp"] >= 150
    assert res["level"] >= 2
    assert "Çırak" in res["badges"]

def test_personality_responses():
    msg = SocialSuiteManager.get_personality_response("success")
    assert isinstance(msg, str)
    assert len(msg) > 0

def test_pvp_duel_creation():
    SocialSuiteManager.init_social_db()
    duel = SocialSuiteManager.create_duel("duel_01", 111, "python")
    assert duel["status"] == "success"
    assert duel["duel_id"] == "duel_01"
