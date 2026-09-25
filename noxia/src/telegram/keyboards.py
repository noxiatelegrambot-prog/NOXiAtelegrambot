from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_approval_keyboard(task_id: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Onayla & Çalıştır", callback_data=f"approve_{task_id}"),
                InlineKeyboardButton(text="❌ İptal Et", callback_data=f"cancel_{task_id}")
            ]
        ]
    )
    return keyboard
