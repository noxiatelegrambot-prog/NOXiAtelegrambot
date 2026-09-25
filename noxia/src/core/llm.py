import os
import aiohttp
from src.core.config import settings

class LLMClient:
    @staticmethod
    async def generate_response(prompt: str, system_prompt: str = "Sen NOXiA otonom yazılım geliştirme ajanısın.") -> str:
        # Eğer gerçek API key yoksa akıllı simülasyon/fallback mekanizması devreye girer
        if not settings.LLM_API_KEY or settings.LLM_API_KEY == "dummy_key":
            return f"[LLM Mock Yanıtı]: '{prompt}' talebiniz için kod/araştırma analizi başarıyla simüle edildi."
            
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {settings.LLM_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": settings.LLM_MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.2
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=payload) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data["choices"][0]["message"]["content"]
                    else:
                        return f"LLM API Hatası: {response.status}"
        except Exception as e:
            return f"LLM Bağlantı Hatası: {str(e)}"
