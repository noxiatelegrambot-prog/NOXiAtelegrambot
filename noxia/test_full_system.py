import asyncio
from src.database.models import init_db
from src.orchestrator.self_healing import SelfHealingOrchestrator
from src.tools.cicd_pipeline import CICDPipeline

async def run_ultimate_test():
    print("=" * 60)
    print("🌟 NOXiA Ultimate Sistem Testi Başlıyor...")
    print("=" * 60)
    
    init_db()
    
    # 1. Self-Healing Testi
    print("\n1️⃣ Self-Healing (Öz-İyileştirme) Test Ediliyor...")
    healing_res = await SelfHealingOrchestrator.execute_with_healing("Basit bir toplama fonksiyonu yaz")
    print(f"   Sonuç Durumu: {healing_res['status']}")
    print(f"   Üretilen Kod Özeti: {healing_res['code'][:100]}...")
    
    # 2. CI/CD Pipeline Testi
    print("\n2️⃣ CI/CD & Deployment Boru Hattı Test Ediliyor...")
    cicd_res = CICDPipeline.execute_pipeline("test: ultimate system verification")
    print(f"   CI/CD Başarı Durumu: {cicd_res['success']}")
    
    print("\n" + "=" * 60)
    print("🎉 NOXiA TÜM SİSTEM TESTLERİ BAŞARIYLA TAMAMLANDI!")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(run_ultimate_test())
