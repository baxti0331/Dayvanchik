from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, filters, ContextTypes
from flask import Flask, request, Response
import asyncio

TOKEN = 8035432614:AAGwZP60-vgZMnSkMoSeZpEWH79UQXrNwLg
bot = Bot(token=TOKEN)
app = Flask(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот, я отвечу на любое сообщение.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

dispatcher = Dispatcher(bot, None, workers=0)
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    asyncio.run(dispatcher.process_update(update))
    return Response("ok", status=200)

if __name__ == "__main__":
    app.run()
