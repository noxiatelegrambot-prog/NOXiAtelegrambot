from app.core.group_games import GroupGamesManager

class GameHandlers:
    @staticmethod
    def handle_bulmaca_command() -> dict:
        puzzle = GroupGamesManager.get_random_word_puzzle()
        return {
            "status": "success",
            "text": f"🔤 **Kelime Bulmaca Başladı!**\n\nKarışık Harfler: `{puzzle['scrambled']}`\nİpucu: {puzzle['hint']}\n\nCevap vermek için: `/tahmin <kelime>`",
            "original": puzzle["original"]
        }

    @staticmethod
    def handle_liderlik_command() -> str:
        board = GroupGamesManager.get_leaderboard(5)
        if not board:
            return "🏆 **Liderlik Tablosu**\n\nHenüz puan alan oyuncu yok. İlk kelimeyi çöz ve zirveye yerleş!"
        
        text = "🏆 **Grup Liderlik Tablosu (Top 5)**\n\n"
        for i, entry in enumerate(board, 1):
            text += f"{i}. {entry['username']} — {entry['score']} Puan\n"
        return text
