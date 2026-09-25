import asyncio
from src.agents.smart_agents import SmartAgents

class SelfHealingOrchestrator:
    @staticmethod
    async def execute_with_healing(task_description: str, max_retries: int = 2) -> dict:
        print(f"🛡️ [Self-Healing] Görev başlatıldı (Max Deneme: {max_retries})")
        
        research = await SmartAgents.researcher_agent(task_description)
        code = await SmartAgents.developer_agent(research)
        
        for attempt in range(max_retries):
            test_report = await SmartAgents.tester_agent(code)
            review_report = await SmartAgents.reviewer_agent(test_report)
            
            # Eğer review veya test başarısız/hatalı derse
            if "hata" in test_report.lower() or "red" in review_report.lower() or "error" in review_report.lower():
                print(f"⚠️ [Self-Healing] Hata tespit edildi, düzeltiliyor (Deneme {attempt + 1}/{max_retries})...")
                fix_prompt = f"Şu inceleme raporundaki hataları düzelt ve kodu yeniden yaz:\n{review_report}\nMevcut Kod:\n{code}"
                code = await SmartAgents.developer_agent(fix_prompt)
            else:
                print("✨ [Self-Healing] Kod başarıyla onaylandı ve testlerden geçti.")
                break
                
        return {
            "code": code,
            "status": "healed_and_approved"
        }
