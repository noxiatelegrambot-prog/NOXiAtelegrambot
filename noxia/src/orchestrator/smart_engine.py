import asyncio
from src.agents.smart_agents import SmartAgents
from src.database.models import db_session

class SmartOrchestrator:
    @staticmethod
    async def run_smart_plan(plan: dict, user_id: int) -> dict:
        task_id = plan["task_id"]
        task_desc = plan.get("intent_raw", "Genel görev")
        
        print(f"🚀 [SmartOrchestrator] Akıllı Task başlatıldı: {task_id}")
        
        # 1. Researcher Adımı
        research_out = await SmartAgents.researcher_agent(task_desc)
        
        # 2. Developer Adımı
        dev_out = await SmartAgents.developer_agent(research_out)
        
        # 3. Tester Adımı
        test_out = await SmartAgents.tester_agent(dev_out)
        
        # 4. Reviewer Adımı
        review_out = await SmartAgents.reviewer_agent(test_out)
        
        results = {
            "task_id": task_id,
            "research": research_out,
            "development": dev_out,
            "testing": test_out,
            "review": review_out,
            "status": "completed"
        }
        
        # Veritabanına kaydet
        with db_session() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT OR REPLACE INTO tasks 
                   (task_id, user_id, intent, status, plan_json, result, updated_at) 
                   VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)""",
                (task_id, user_id, plan.get("intent", "general"), "completed", str(plan), str(results))
            )
            
        print(f"✅ [SmartOrchestrator] Akıllı Task tamamlandı: {task_id}")
        return results
