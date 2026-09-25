import asyncio
from src.database.models import init_db
from src.intent.parser import IntentParser
from src.memory.manager import MemoryManager
from src.planner.engine import TaskPlanner
from src.orchestrator.engine import Orchestrator

async def main():
    print("--- NOXiA Test Başlıyor ---")
    
    # 1. DB Başlat
    init_db()
    
    # 2. Örnek Kullanıcı Girdisi
    user_id = 12345
    user_input = "Python ile Telegram botu için kod yaz"
    print(f"Kullanıcı Girdisi: {user_input}")
    
    # 3. Intent Analizi
    intent_data = IntentParser.parse(user_input)
    print(f"Algılanan Niyet: {intent_data}")
    
    # 4. Belleğe Kaydet
    MemoryManager.save_memory(user_id, "user_input", user_input)
    
    # 5. Plan Yap
    plan = TaskPlanner.create_plan(intent_data)
    print(f"Oluşturulan Plan:\n{plan}")
    
    # 6. Orchestrator ile Çalıştır
    await Orchestrator.run_plan(plan, user_id)
    print("--- NOXiA Test Tamamlandı ---")

if __name__ == "__main__":
    asyncio.run(main())
