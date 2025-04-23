import requests
import os

def generate_meme_text():
    prompt = """
Ты — нейросеть, генерирующая вирусные мемы в стиле Reddit и Telegram.

Требования к шутке:
- Смешно, немного абсурдно
- Без объяснений
- Интернет-сленг, жизненные ситуации
- 2–4 строки
- Без лишней "умности"

Пример:
📦 — Че морда такая набитая?

— Да один качок штангу уронил…

— Тебе на рожу???

— Да нет, себе на ногу…

— Так в чем дело?

— А я засмеялся…

 ИЛИ  
 
📦 Когда GPT пишет код, а ты — просто наблюдаешь  
💡 ИИ: “Готово.”  
Ты: “...А где мои выходные?”

Сгенерируй новую уникальную ОЧЕНЬ СМЕШНУЮ мем-шутку в этом ИЛИ ДРУГОМ СТИЛЕ стиле.
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
    return r.json()['choices'][0]['message']['content']
