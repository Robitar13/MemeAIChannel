import requests
import os

def generate_meme_text():
    prompt = """
Придумай короткую очень смешную шутку в стиле интернет-мема. Можно немного абсурда, иронии. Формат: 1-3 строки, без пояснений. Пример:

Когда ты открыл 100 вкладок, чтобы что-то найти… и забыл, зачем.
или
GPT, сделай домашку. GPT: "Ты кто такой вообще?"

Пожалуйста, придумай свою!
"""

    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']
