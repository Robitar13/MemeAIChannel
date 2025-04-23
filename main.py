import os
import requests
import random
from dotenv import load_dotenv
from utils.meme_prompts import generate_meme_text
from utils.image_gen import generate_image_url

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
UNSPLASH_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

def send_meme(text, image_url):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    data = {
        "chat_id": CHANNEL,
        "caption": text,
        "photo": image_url,
        "parse_mode": "HTML"
    }
    requests.post(url, data=data)

def main():
    meme_text = generate_meme_text()
    image_url = generate_image_url(meme_text)
    send_meme(meme_text, image_url)

if __name__ == "__main__":
    main()
