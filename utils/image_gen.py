import requests
import os

def generate_image_url(query="funny ai meme"):
    url = f"https://api.unsplash.com/search/photos?query={query}&client_id={os.getenv('UNSPLASH_ACCESS_KEY')}"
    r = requests.get(url)
    data = r.json()
    if data.get("results"):
        return data["results"][0]["urls"]["regular"]
    return "https://i.imgur.com/Z6hZ6OQ.png"  # запасная картинка
