import os
import requests
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "").strip()

def get_weather_data(city):
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={city}"
        f"&appid={WEATHER_API_KEY}&lang=pt_br&units=metric"
    )
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[DEBUG] Erro na API: {response.status_code} - {response.text}")
            return None
    except requests.RequestException as e:
        print(f"[DEBUG] Erro na conexão: {e}")
        return None
