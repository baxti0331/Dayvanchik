from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔍 Начать знакомство", callback_data="start_match")],
        [InlineKeyboardButton("📖 Правила", url="https://example.com/rules")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "👋 Привет! Я — твой помощник в мире знакомств ❤️\n\n"
        "📌 Заполни анкету, оценивай других и находи совпадения!\n"
        "Готов начать?"
    )

    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

if __name__ == "__main__":
    from telegram.ext import CallbackQueryHandler

    async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()

        if query.data == "start_match":
            await query.edit_message_text("🚀 Отлично! Давай начнём подбор 😊")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()