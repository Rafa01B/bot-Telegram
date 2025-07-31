from models.weather_model import get_weather_data
from views.weather_view import format_weather_message

def get_weather_for_city(city: str) -> str:
    print(f"[DEBUG] Buscando clima para: {city}")
    data = get_weather_data(city)
    print(f"[DEBUG] Dados recebidos: {data}")
    if data is None:
        return "❌ Cidade não encontrada ou erro ao obter dados do clima."
    return format_weather_message(data)
