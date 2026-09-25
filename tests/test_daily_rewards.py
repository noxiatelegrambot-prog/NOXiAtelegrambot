from app.core.daily_rewards import DailyRewardsManager
from app.core.social_suite import SocialSuiteManager

def test_daily_reward_claim():
    SocialSuiteManager.init_social_db()
    res = DailyRewardsManager.claim_daily_bonus(54321, "seri_test_user")
    assert res["status"] == "success"
    assert res["reward_xp"] >= 50
    assert res["streak"] >= 1

    # Claiming again on the same day should return already_claimed
    res2 = DailyRewardsManager.claim_daily_bonus(54321, "seri_test_user")
    assert res2["status"] == "already_claimed"
