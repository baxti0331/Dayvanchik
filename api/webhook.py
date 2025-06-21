import os
from telebot import TeleBot, types

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
bot = TeleBot(API_TOKEN)

# Простые ответы
@bot.message_handler(func=lambda msg: True)
def reply(message):
    text = message.text.lower()
    if "привет" in text:
        bot.send_message(message.chat.id, "Привет! 👋")
    elif "как дела" in text:
        bot.send_message(message.chat.id, "Хорошо, спасибо! А у тебя?")
    elif "что делаешь" in text:
        bot.send_message(message.chat.id, "Жду, когда ты напишешь 😉")
    else:
        bot.send_message(message.chat.id, "Не понял тебя 😅")

def handler(request):
    if request.method != "POST":
        return "Only POST allowed", 405

    if request.headers.get("content-type") == "application/json":
        json_str = request.get_data().decode("utf-8")
        update = types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return "", 200
    else:
        return "Forbidden", 403
