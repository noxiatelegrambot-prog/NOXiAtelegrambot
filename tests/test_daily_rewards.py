from app.core.daily_rewards import DailyRewardsManager
from app.core.social_suite import SocialSuiteManager
import random

def test_daily_reward_claim():
    SocialSuiteManager.init_social_db()
    unique_user_id = random.randint(100000, 999999)
    
    res = DailyRewardsManager.claim_daily_bonus(unique_user_id, "seri_test_user")
    assert res["status"] == "success"
    assert res["reward_xp"] >= 50
    assert res["streak"] >= 1

    # Claiming again on the same day should return already_claimed
    res2 = DailyRewardsManager.claim_daily_bonus(unique_user_id, "seri_test_user")
    assert res2["status"] == "already_claimed"
