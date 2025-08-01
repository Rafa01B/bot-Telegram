import os
import asyncio
import nest_asyncio 
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from controllers.bot_controller import start, help_command, handle_message
from flask import Flask
from threading import Thread

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "🤖 Bot está online!"

def run_flask():
    port = int(os.environ.get("PORT", 8000))
    flask_app.run(host="0.0.0.0", port=port)


async def run_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot rodando...")
    await app.run_polling()


if __name__ == "__main__":
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    loop = asyncio.get_event_loop()
    nest_asyncio.apply(loop)  
    loop.run_until_complete(run_bot())
