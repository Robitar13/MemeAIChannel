import requests
import os

def generate_meme_text():
    prompt = """
Ты — нейросеть, генерирующая вирусные мемы в Telegram.

Придумай короткую, очень смешную и абсурдную шутку (мем). Затем придумай, какую сцену можно изобразить как картинку к этой шутке.

Формат ответа:
📝 Мем-текст: [шутка]
🖼 Картинка: [описание сцены]
"""

    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",  # можно заменить на openai/gpt-4
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        r = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        result = r.json()

        if "choices" not in result:
            print("❌ Ошибка от OpenRouter:", result)
            return "📝 Мем не сгенерирован", "🖼 Картинка отсутствует"

        content = result['choices'][0]['message']['content']
        lines = content.splitlines()

        meme_text = next((l.replace("📝 Мем-текст:", "").strip() for l in lines if l.startswith("📝")), "📝 Мем не найден")
        image_prompt = next((l.replace("🖼 Картинка:", "").strip() for l in lines if l.startswith("🖼")), "🖼 Сцена не указана")

        return meme_text, image_prompt

    except Exception as e:
        print("❌ Ошибка обработки:", e)
        return "📝 Мем не сгенерирован", "🖼 Ошибка"
