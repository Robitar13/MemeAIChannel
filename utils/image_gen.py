import requests
import os

def generate_image(prompt):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/dall-e-3",  # важно!
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }

    response = requests.post("https://openrouter.ai/api/v1/images/generations", headers=headers, json=data)
    result = response.json()

    try:
        return result["data"][0]["url"]
    except Exception as e:
        print("❌ Ошибка генерации изображения:", result)
        return None  # не подставлять imgur-заглушку

