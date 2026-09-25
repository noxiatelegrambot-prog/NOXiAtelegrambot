class EngagementAnalyticsEngine:
    def __init__(self):
        self.user_stats = {}

    def record_interaction(self, user_id: str, message_length: int, sentiment: str) -> dict:
        if user_id not in self.user_stats:
            self.user_stats[user_id] = {"total_messages": 0, "engagement_score": 0, "positive_count": 0}
        
        stats = self.user_stats[user_id]
        stats["total_messages"] += 1
        
        # Calculate dynamic engagement score increment based on depth and sentiment
        increment = max(1, message_length // 10)
        if sentiment == "positive":
            increment += 5
            stats["positive_count"] += 1
            
        stats["engagement_score"] += increment
        
        return {
            "user_id": user_id,
            "total_messages": stats["total_messages"],
            "engagement_score": stats["engagement_score"]
        }

    def get_analytics(self, user_id: str) -> dict:
        return self.user_stats.get(user_id, {"total_messages": 0, "engagement_score": 0, "positive_count": 0})
