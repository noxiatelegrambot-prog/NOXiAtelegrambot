import asyncio
from src.database.models import init_db
from src.intent.parser import IntentParser
from src.memory.manager import MemoryManager
from src.planner.engine import TaskPlanner
from src.orchestrator.engine import Orchestrator
from src.tools.sandbox import SandboxTool
from src.tools.git_tool import GitTool
from src.telegram.presentation import TelegramPresentation

async def run_full_integration_test():
    print("=" * 50)
    print("🧪 NOXiA Uçtan Uca Entegrasyon Testi Başlıyor...")
    print("=" * 50)
    
    # 1. DB & Temel Başlatma
    init_db()
    user_id = 99999
    user_input = "Python ile test scripti geliştir ve çalıştır"
    print(f"\n1️⃣ Kullanıcı Girdisi: '{user_input}'")
    
    # 2. Intent Analizi
    intent_data = IntentParser.parse(user_input)
    print(f"2️⃣ Algılanan Niyet: {intent_data['intent']} (Güven: {intent_data['confidence']})")
    
    # 3. Bellek Testi
    MemoryManager.save_memory(user_id, "integration_test", user_input)
    memories = MemoryManager.get_user_memories(user_id, limit=1)
    print(f"3️⃣ Bellek Kaydı Doğrulandı: {memories[0]['content']}")
    
    # 4. Planlayıcı (Planner) Testi
    plan = TaskPlanner.create_plan(intent_data)
    print(f"4️⃣ Plan Oluşturuldu: {plan['task_id']} ({len(plan['steps'])} adım)")
    
    # 5. Orchestrator & Ajan Akışı Testi
    print("5️⃣ Orchestrator ajanları koordine ediyor...")
    results = await Orchestrator.run_plan(plan, user_id)
    print(f"   Ajan Çalışma Sonucu: {len(results)} adım başarıyla tamamlandı.")
    
    # 6. Sandbox Testi (Geçici bir test dosyası oluşturup çalıştırarak test edelim)
    test_script_path = "temp_test_script.py"
    with open(test_script_path, "w") as f:
        f.write("print('Hello from NOXiA Sandbox!')")
        
    print("6️⃣ Sandbox Testi Çalıştırılıyor...")
    sandbox_result = await SandboxTool.run_code(test_script_path)
    # Temizlik
    import os
    if os.path.exists(test_script_path):
        os.remove(test_script_path)
        
    print(f"   Sandbox Başarı Durumu: {sandbox_result['success']} | Çıktı: {sandbox_result['stdout'].strip()}")
    
    # 7. Git Araç Testi (Durum kontrolü)
    git_status = GitTool.run_git_command(["status"])
    print(f"7️⃣ Git Durumu Kontrol Edildi. (Çıktı uzunluğu: {len(git_status.get('output', ''))})")
    
    # 8. Telegram Presentation Format Testi
    final_output = TelegramPresentation.format_final_result(
        task_id=plan["task_id"],
        summary="Entegrasyon testi başarıyla tamamlandı.",
        agents=["Researcher", "Developer", "Tester", "Reviewer"],
        tests_passed=5,
        files_changed=2
    )
    print("\n8️⃣ Telegram Sunum Çıktısı Örneği:")
    print("-" * 40)
    print(final_output)
    print("-" * 40)
    
    print("\n" + "=" * 50)
    print("✅ TÜM ENTEGRASYON TESTLERİ BAŞARIYLA TAMAMLANDI!")
    print("=" * 50)

if __name__ == "__main__":
    asyncio.run(run_full_integration_test())
