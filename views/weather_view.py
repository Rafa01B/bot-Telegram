def format_weather_message(data):

    desc = data['weather'][0]['description'].capitalize()
    temp = data['main']['temp']
    feels = data['main']['feels_like']
    humidity = data['main']['humidity']

    message = (
        f"🌤️ Clima em {data['name']}:\n"
        f"- Descrição: {desc}\n"
        f"- Temperatura: {temp}°C\n"
        f"- Sensação térmica: {feels}°C\n"
        f"- Umidade: {humidity}%\n\n"
        f"- Autora: Rafaela Bezerra Rodrigues"

    )
    return message
