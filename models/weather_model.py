import os
import requests
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&lang=pt_br&units=metric"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None
        return response.json()
    except Exception:
        return None
