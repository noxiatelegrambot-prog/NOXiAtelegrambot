class ProactiveEngagementEngine:
    @staticmethod
    def generate_proactive_prompt(user_interests: list) -> dict:
        # Generate engaging conversational hooks based on user's known interests
        if not user_interests:
            return {
                "status": "default",
                "hook": "Bugün hangi projeler üzerinde çalışıyoruz? Yeni fikirler var mı?"
            }
        
        primary_interest = user_interests[0]
        return {
            "status": "success",
            "interest_targeted": primary_interest,
            "hook": f"Geçenlerde bahsettiğimiz {primary_interest} konusunda yeni bir gelişme var mı, ne dersin?"
        }
