from telegram import Update
from telegram.ext import ContextTypes
from controllers.weather_controller import get_weather_for_city

def tratar_nome_cidade(nome):
    partes = nome.split(',')
    if len(partes) == 2:
        cidade, uf = partes[0].strip(), partes[1].strip().upper()
        if len(uf) == 2:
            return f"{cidade},BR"
    return nome

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Olá! Me envie a mensagem:\n\n"
        "Clima [cidade]\n"
        "Ex: Clima Recife\n\n"
        "📌 Dica:\n"
        "- Para cidades com mesmo nome, use cidade,UF ou cidade,PAÍS\n"
        "Ex: Clima Porto Alegre,RS ou Clima Paris,FR\n\n"
        "⚠️ Se usar UF (ex: PE), o bot assume Brasil."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Comandos disponíveis:\n"
        "/start - Início\n"
        "/help - Ajuda\n\n"
        "ℹ️ Como usar:\n"
        "Clima [cidade]\n"
        "Ex: Clima Recife\n\n"
        "❗ Dica:\n"
        "Se a cidade tiver nomes repetidos, você pode usar:\n"
        "- Cidade,UF (ex: Clima Recife,PE)\n"
        "- Ou Cidade,PAÍS (ex: Clima Paris,FR)\n\n"
        "⚠️ Por padrão, 'cidade,UF' busca no Brasil.\n"
        "Para outros países, use 'cidade,PAÍS'."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text

    print(f"[MSG] {user.username or user.first_name}: {text}")

    if text.lower().startswith("clima "):
        city_input = text[6:].strip()
        cidade_tratada = tratar_nome_cidade(city_input)

        print(f"[DEBUG] Cidade solicitada: {city_input}")
        print(f"[DEBUG] Cidade tratada: {cidade_tratada}")


        response = get_weather_for_city(cidade_tratada)
        await update.message.reply_text(response)
    else:
        await update.message.reply_text("❗ Use o formato: Clima [cidade] ou Clima cidade,UF/PAÍS")
