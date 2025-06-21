from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Ответ на команду /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я обычный бот для общения. Напиши мне что-нибудь!")

# Ответ на любое текстовое сообщение
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_received = update.message.text
    await update.message.reply_text(f"Ты сказал: {text_received}")

# Главная функция запуска бота
async def main():
    app = ApplicationBuilder().token("ТВОЙ_ТОКЕН_ОТСЮДА").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Бот запущен...")
    await app.run_polling()

# Запуск
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
