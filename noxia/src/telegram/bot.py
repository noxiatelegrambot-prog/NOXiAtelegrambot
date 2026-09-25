import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from src.core.config import settings
from src.database.models import init_db
from src.intent.parser import IntentParser
from src.memory.manager import MemoryManager
from src.planner.engine import TaskPlanner
from src.orchestrator.engine import Orchestrator

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    welcome_text = (
        "🤖 **NOXiA Autonomous Platform'a Hoş Geldiniz!**\n\n"
        "Ben otonom yazılım geliştirme ve araştırma asistanınızım.\n"
        "Bana bir görev yazın (örn: *'Python ile Telegram botu için kod yaz'*), "
        "arkada plan yapıp ajanlarımı çalıştırayım."
    )
    await message.answer(welcome_text, parse_mode="Markdown")

@dp.message(F.text)
async def handle_user_message(message: Message):
    user_id = message.from_user.id
    user_text = message.text
    
    await message.answer(f"⏳ **Niyet analiz ediliyor ve plan yapılıyor...**", parse_mode="Markdown")
    
    # 1. Intent Analizi
    intent_data = IntentParser.parse(user_text)
    
    # 2. Belleğe Kaydet
    MemoryManager.save_memory(user_id, "user_input", user_text)
    
    # 3. Plan Yap
    plan = TaskPlanner.create_plan(intent_data)
    
    # 4. Kullanıcıya Planı Göster
    plan_msg = f"📋 **Görev Planı Oluşturuldu** (`{plan['task_id']}`)\n\n"
    for step in plan["steps"]:
        plan_msg += f"{step['step']}. 🤖 **{step['agent']}**: {step['action']}\n"
    plan_msg += "\n🚀 **Ajanlar işe koyuluyor...**"
    
    await message.answer(plan_msg, parse_mode="Markdown")
    
    # 5. Orchestrator ile Çalıştır
    results = await Orchestrator.run_plan(plan, user_id)
    
    # 6. Sonucu Telegram'a Raporla
    result_msg = (
        f"✅ **Görev Başarıyla Tamamlandı!**\n"
        f"🆔 `{plan['task_id']}`\n\n"
        f"🤖 **Çalışan Ajanlar:** Researcher → Developer → Tester → Reviewer\n"
        f"📊 **Durum:** Tüm adımlar başarıyla yürütüldü."
    )
    await message.answer(result_msg, parse_mode="Markdown")

async def main():
    init_db()
    print("🤖 Telegram Bot başlatılıyor...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
