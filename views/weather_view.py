def format_weather_message(data):
    nome = data.get("name")
    clima = data["weather"][0]["description"].capitalize()
    temp = data["main"]["temp"]
    sensacao = data["main"]["feels_like"]
    umidade = data["main"]["humidity"]

    mensagem = (
        f"🌤️ Clima em {nome}:\n"
        f"- Descrição: {clima}\n"
        f"- Temperatura: {temp}ºC\n"
        f"- Sensação térmica: {sensacao}ºC\n"
        f"- Umidade: {umidade}%"
    )
    return mensagem
