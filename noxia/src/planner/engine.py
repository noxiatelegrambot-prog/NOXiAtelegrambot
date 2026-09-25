import json
import uuid

class TaskPlanner:
    @staticmethod
    def create_plan(intent_data: dict) -> dict:
        task_id = f"task_{uuid.uuid4().hex[:8]}"
        intent = intent_data.get("intent")
        
        steps = []
        if intent == "development":
            steps = [
                {"step": 1, "agent": "Researcher", "action": "Gerekli doküman ve kütüphaneleri incele"},
                {"step": 2, "agent": "Developer", "action": "Kod değişikliklerini yap ve yama oluştur"},
                {"step": 3, "agent": "Tester", "action": "Sandbox ortamında testleri çalıştır"},
                {"step": 4, "agent": "Reviewer", "action": "Kod kalitesi ve güvenlik incelemesi yap"}
            ]
        elif intent == "research":
            steps = [
                {"step": 1, "agent": "Researcher", "action": "Web ve kaynak taraması yap"},
                {"step": 2, "agent": "Reviewer", "action": "Bulguları özetle ve raporla"}
            ]
        else:
            steps = [
                {"step": 1, "agent": "GeneralChat", "action": "Doğrudan yanıt ver"}
            ]
            
        plan = {
            "task_id": task_id,
            "intent": intent,
            "steps": steps,
            "status": "planned"
        }
        
        return plan
