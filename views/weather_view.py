def format_weather_message(data):
    try:
        cidade = data.get("name", "Cidade desconhecida")
        pais = data.get("sys", {}).get("country", "")
        descricao = data.get("weather", [{}])[0].get("description", "").capitalize()
        temperatura = round(data.get("main", {}).get("temp", 0))
        sensacao = round(data.get("main", {}).get("feels_like", 0))
        umidade = data.get("main", {}).get("humidity", 0)

        mensagem = (
            f"🌤️ Clima em {cidade}, {pais}:\n"
            f"- Descrição: {descricao}\n"
            f"- Temperatura: {temperatura}°C\n"
            f"- Sensação térmica: {sensacao}°C\n"
            f"- Umidade: {umidade}%"
        )
        return mensagem
    except Exception as e:
        print(f"[DEBUG] Erro ao formatar mensagem: {e}")
        return "❌ Erro ao formatar os dados do clima."
