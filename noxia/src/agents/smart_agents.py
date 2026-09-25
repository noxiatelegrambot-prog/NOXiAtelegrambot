from src.core.llm import LLMClient

class SmartAgents:
    @staticmethod
    async def researcher_agent(task_description: str) -> str:
        prompt = f"Şu görev için gerekli dokümantasyon, kütüphane ve teknik gereksinimleri araştır ve listele: {task_description}"
        return await LLMClient.generate_response(prompt, "Sen uzman bir Araştırmacı Ajanısın.")

    @staticmethod
    async def developer_agent(research_notes: str) -> str:
        prompt = f"Şu araştırma notlarına ve isteğe dayanarak temiz ve çalışır Python kodu yaz:\n{research_notes}"
        return await LLMClient.generate_response(prompt, "Sen uzman bir Python Geliştirici Ajanısın. Sadece çalıştırılabilir kod blokları üret.")

    @staticmethod
    async def tester_agent(code_content: str) -> str:
        prompt = f"Şu kodu test senaryoları açısından incele, olası hataları bul ve test raporu oluştur:\n{code_content}"
        return await LLMClient.generate_response(prompt, "Sen titiz bir Test ve QA Ajanısın.")

    @staticmethod
    async def reviewer_agent(test_results: str) -> str:
        prompt = f"Şu test sonuçlarına göre kod kalitesini, güvenliği ve mimariyi değerlendir. Onay ver veya düzeltme iste:\n{test_results}"
        return await LLMClient.generate_response(prompt, "Sen kıdemli bir Kod İnceleme (Reviewer) Ajanısın.")
