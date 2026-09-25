import asyncio
from src.database.models import db_session

class Orchestrator:
    @staticmethod
    async def run_plan(plan: dict, user_id: int):
        task_id = plan["task_id"]
        steps = plan["steps"]
        
        print(f"🚀 [Orchestrator] Task başlatıldı: {task_id}")
        results = []
        
        for step in steps:
            agent_name = step["agent"]
            action = step["action"]
            print(f"🤖 [{agent_name}] Çalışıyor: {action}")
            
            # Simüle edilmiş ajan işleme süreci (İleride gerçek araçlarla dolacak)
            await asyncio.sleep(0.5)
            
            results.append({
                "step": step["step"],
                "agent": agent_name,
                "action": action,
                "status": "completed"
            })
            
        # Veritabanına görev sonucunu kaydet
        with db_session() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT OR REPLACE INTO tasks 
                   (task_id, user_id, intent, status, plan_json, result, updated_at) 
                   VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)""",
                (task_id, user_id, plan.get("intent", "general"), "completed", str(plan), str(results))
            )
        
        print(f"✅ [Orchestrator] Task başarıyla tamamlandı: {task_id}")
        return results
