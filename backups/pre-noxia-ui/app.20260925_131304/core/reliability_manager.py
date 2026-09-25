class ReliabilityManager:
    @staticmethod
    def format_safe_error(exception_msg: str) -> str:
        # Hide internal traceback details from users, return clean safe message
        return "⚠️ Beklenmeyen bir sistem hatası oluştu. İşlem güvenli bir şekilde durduruldu."

    @staticmethod
    def chunk_long_message(text: str, max_length: int = 4096) -> list:
        if len(text) <= max_length:
            return [text]
        return [text[i:i + max_length] for i in range(0, len(text), max_length)]
