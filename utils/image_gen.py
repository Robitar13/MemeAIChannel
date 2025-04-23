import requests
import os

def generate_image(prompt):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/dall-e-3",  # или другой подходящий image endpoint
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }

    r = requests.post("https://openrouter.ai/api/v1/images/generations", headers=headers, json=data)
    try:
        return r.json()["data"][0]["url"]
    except Exception as e:
        print("❌ Ошибка генерации картинки:", e)
        return "https://i.imgur.com/Z6hZ6OQ.png"  # запасная

