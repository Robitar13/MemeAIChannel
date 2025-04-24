import os
import requests
from dotenv import load_dotenv
from utils.meme_prompts import generate_meme_text
from utils.image_gen import generate_image

# Загружаем переменные окружения из .env (или GitHub Secrets)
load_dotenv()

# Получаем токены и данные
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
UNSPLASH_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

# Функция отправки мема в Telegram
def send_meme(meme_text, image_url):
    print("📤 Отправляем мем в Telegram...")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    payload = {
        "chat_id": CHANNEL_USERNAME,
        "photo": image_url,
        "caption": meme_text,
        "parse_mode": "HTML"
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("✅ Мем успешно опубликован!")
    else:
        print(f"⚠️ Ошибка публикации: {response.status_code}")
        print(response.text)

# Главная логика
def main():
    print("🤖 Генерируем шутку...")
    meme_text, image_prompt = generate_meme_text()
    print(f"📝 Шутка: {meme_text}")
    print(f"🖼 Запрос к DALL·E: {image_prompt}")

    image_url = generate_image(image_prompt)

    if image_url:
        send_meme(meme_text, image_url)
    else:
        print("⚠️ Картинка не сгенерирована. Пропускаем публикацию.")

# Запуск
if __name__ == "__main__":
    main()

