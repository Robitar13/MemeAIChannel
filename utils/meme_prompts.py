import requests
import os

def generate_meme_text():
    prompt = """
Придумай очень смешной интернет-мем в формате Telegram-поста.

1. Придумай короткую, абсурдную и жизненную шутку в стиле Reddit / Пикабу
2. Придумай, какую сцену (ситуацию/персонажа) нужно изобразить на картинке, чтобы она визуально отражала мем


Требования к шутке:
- Смешно, немного абсурдно
- Без объяснений
- Интернет-сленг, жизненные ситуации
- 2–4 строки
- Без лишней "умности"

Формат ответа:

🖼 Картинка: [описание сцены, которую можно сгенерировать]
📝 Мем-текст: [шутка]

Пример:

🖼 Картинка: Робот в галстуке держит в руках лист бумаги и плачет перед монитором
📝 Мем-текст: Когда GPT написал код, но забыл, зачем он тебе вообще
Сгенерируй новый вариант:
"""

    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }

    r = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    text = r.json()['choices'][0]['message']['content']

    # Разделим мем и описание сцены
    lines = text.strip().split("\n")
    meme_line = next((l for l in lines if l.startswith("📝")), "📝 Мем-текст: (мем не найден)")
    image_line = next((l for l in lines if l.startswith("🖼")), "🖼 Картинка: (описание не найден)")

    meme_text = meme_line.replace("📝 Мем-текст:", "").strip()
    image_prompt = image_line.replace("🖼 Картинка:", "").strip()

    return meme_text, image_prompt

