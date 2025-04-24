import requests
import os

def generate_image(prompt):
    api_key = os.getenv("GENAPI_API_KEY")  # ты должен добавить это в .env или GitHub Secrets

    url = "https://gen-api.ru/model/dalle-3/api"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "prompt": prompt,
        "quality": "standard",  # или "hd"
        "n": 1,
        "size": "1024x1024"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        result = response.json()

        if "data" in result and result["data"]:
            return result["data"][0]["url"]  # картинка найдена
        else:
            print("⚠️ Не удалось получить изображение:", result)
            return None

    except Exception as e:
        print("❌ Ошибка генерации изображения:", e)
        return None
