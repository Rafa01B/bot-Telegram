from models.weather_model import get_weather_data
from views.weather_view import format_weather_message

def get_weather_for_city(city):
    data = get_weather_data(city)
    if not data:
        return "❌ Não consegui encontrar a cidade ou ocorreu um erro na consulta."
    
    if data.get("cod") != 200:
        return f"❌ Erro: {data.get('message', 'Cidade não encontrada')}"

    return format_weather_message(data)
