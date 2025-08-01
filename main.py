import os
import threading
from flask import Flask
from telegram.ext import Application, CommandHandler, MessageHandler, filters

app = Flask(__name__)

@app.route("/")
def home():
    return "🤖 Bot online!"

def run_flask():
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

async def run_bot():
    from controllers.bot_controller import start, help_command, handle_message

    bot_app = Application.builder().token(os.getenv("TELEGRAM_TOKEN")).build()

    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(CommandHandler("help", help_command))
    bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    await bot_app.run_polling()

if __name__ == "__main__":
    import asyncio

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    asyncio.run(run_bot())
