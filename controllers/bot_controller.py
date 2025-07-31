from telegram import Update
from telegram.ext import CallbackContext
from controllers.weather_controller import get_weather_for_city

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Olá! Me envie 'Clima [cidade]' para receber a previsão do tempo.")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Comandos disponíveis:\n/start - Início\n/help - Ajuda\n\nUse: Clima [cidade]")

def handle_message(update: Update, context: CallbackContext):
    user = update.effective_user
    text = update.message.text

    print(f"[MSG] {user.username or user.first_name}: {text}")

    if text.lower().startswith("clima "):
        city = text[6:].strip()
        response = get_weather_for_city(city)
        update.message.reply_text(response)
    else:
        update.message.reply_text("❗ Use o formato: Clima [cidade]")
