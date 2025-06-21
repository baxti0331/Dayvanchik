from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔍 Начать знакомство", callback_data="start_match")],
        [InlineKeyboardButton("📢Спонсор1", url="https://t.me/kinoseriallivbot")],
        [InlineKeyboardButton("📢 Спонсор2", url="https://t.me/kinoseriallivbot")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "👋 Привет! Для начала нужно подписаться на наших спонсоров.\n\n"
        "📌 После этого сможешь заполнить анкету, оценивать других и находить совпадения!\n"
        "Готов начать?"
    )

    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "start_match":
        await query.edit_message_text("🚀 Отлично! Сейчас подберу тебе кого-нибудь 😊")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Бот запущен!")
    app.run_polling()