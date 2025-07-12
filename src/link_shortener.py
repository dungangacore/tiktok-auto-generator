import requests
from config import SHORTENER_API_KEY

class LinkShortener:
    def shorten(self, url: str) -> str:
        endpoint = f"https://ouo.io/api/{SHORTENER_API_KEY}?s={url}"
        try:
            response = requests.get(endpoint)
            return response.text.strip()
        except:
            return "Failed to shorten URL"
