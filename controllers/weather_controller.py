from models.weather_model import get_weather_data
from views.weather_view import format_weather_message

def get_weather_for_city(city):
    data = get_weather_data(city)
    print(f"[DEBUG] Dados recebidos da API: {data}")

    if data and str(data.get("cod")) == "200":
        return format_weather_message(data)
    else:
        return "❌ Cidade não encontrada ou erro ao obter dados do clima."
