import os
import requests
import random
from dotenv import load_dotenv
from utils.meme_prompts import generate_meme_text
from utils.image_gen import generate_image
import requests

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
UNSPLASH_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

def send_meme(text, image_url):
    print("🖼 Отправляем мем в Telegram...")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    data = {
        "chat_id": CHANNEL_USERNAME,
        "photo": image_url,
        "caption": text,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=data)
    print("✅ Ответ Telegram:", response.status_code)
    
def main():
    print("🤖 Генерируем мем...")
    meme_text, image_prompt = generate_meme_text()
    print("🎨 Генерируем картинку по сцене:", image_prompt)
    meme_image = generate_image(image_prompt)
    send_meme(meme_text, meme_image)
meme_image = generate_image(image_prompt)

if meme_image:
    send_meme(meme_text, meme_image)
else:
    print("⚠️ Картинка не сгенерирована. Пропускаем пост.")

if __name__ == "__main__":
    main()
