from app.core.engagement_analytics import EngagementAnalyticsEngine

def test_engagement_recording():
    engine = EngagementAnalyticsEngine()
    user = "user_analytics_1"

    res = engine.record_interaction(user, 50, "positive")
    assert res["total_messages"] == 1
    assert res["engagement_score"] > 0

    analytics = engine.get_analytics(user)
    assert analytics["positive_count"] == 1

def test_nonexistent_user_analytics():
    engine = EngagementAnalyticsEngine()
    analytics = engine.get_analytics("ghost_user")
    assert analytics["total_messages"] == 0
    assert analytics["engagement_score"] == 0
