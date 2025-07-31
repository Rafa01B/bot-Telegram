from telegram import Update
from telegram.ext import ContextTypes

from controllers.weather_controller import get_weather_for_city

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Me envie 'Clima [cidade]' para receber a previsão.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text.lower().startswith("clima") or text.lower().startswith("tempo"):
        parts = text.split(" ", 1)
        if len(parts) == 2:
            city = parts[1]
            weather_message = get_weather_for_city(city)
            await update.message.reply_text(weather_message)
        else:
            await update.message.reply_text("Digite: Clima [nome da cidade]")
    else:
        await update.message.reply_text("Use: Clima [cidade] para obter a previsão.")
