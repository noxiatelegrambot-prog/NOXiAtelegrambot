class Planner:
    RESEARCH_WORDS = (
        "araştır", "araştirma", "search", "research",
        "incele", "bul", "öğren", "ogren"
    )

    CODE_WORDS = (
        "kod", "yaz", "geliştir", "gelistir", "düzelt",
        "fix", "implement", "oluştur", "olustur"
    )

    TEST_WORDS = (
        "test", "kontrol", "doğrula", "dogrula",
        "denetle", "hata", "bug"
    )

    def create_plan(self, prompt: str) -> list[str]:
        text = prompt.lower()

        plan = ["analyze"]

        if any(word in text for word in self.RESEARCH_WORDS):
            plan.append("research")

        if any(word in text for word in self.CODE_WORDS):
            plan.append("develop")

        if any(word in text for word in self.TEST_WORDS):
            plan.append("test")

        if len(plan) == 1:
            plan.extend(["plan", "execute", "verify"])

        elif "test" not in plan:
            plan.append("verify")

        return plan
