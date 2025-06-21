const express = require('express')
const axios = require('axios')

const app = express()
const port = process.env.PORT || 4000
const TOKEN = process.env.BOT_TOKEN
const TELEGRAM_API = `https://api.telegram.org/bot${TOKEN}`

app.use(express.json())

app.post(`/webhook/${TOKEN}`, async (req, res) => {
  const update = req.body

  if (!update.message) {
    return res.sendStatus(200)
  }

  const chatId = update.message.chat.id
  const text = update.message.text

  if (text === '/start') {
    const replyMarkup = {
      inline_keyboard: [
        [{ text: "🔍 Начать знакомство", callback_data: "start_match" }],
        [{ text: "📖 Правила", url: "https://example.com/rules" }],
        [{ text: "📢 Спонсоры", url: "https://t.me/your_sponsor_channel" }]
      ]
    }

    await axios.post(`${TELEGRAM_API}/sendMessage`, {
      chat_id: chatId,
      text:
        "👋 Привет! Для начала нужно подписаться на наших спонсоров.\n\n" +
        "📌 После этого сможешь заполнить анкету, оценивать других и находить совпадения!\n" +
        "Готов начать?",
      reply_markup: replyMarkup,
    })
  } else if (update.callback_query) {
    const callbackData = update.callback_query.data
    const callbackChatId = update.callback_query.message.chat.id
    const callbackMessageId = update.callback_query.message.message_id

    if (callbackData === 'start_match') {
      await axios.post(`${TELEGRAM_API}/editMessageText`, {
        chat_id: callbackChatId,
        message_id: callbackMessageId,
        text: '🚀 Отлично! Сейчас подберу тебе кого-нибудь 😊',
      })

      // Ответить на callback, чтобы убрать "часики" у кнопки
      await axios.post(`${TELEGRAM_API}/answerCallbackQuery`, {
        callback_query_id: update.callback_query.id
      })
    }
  }

  res.sendStatus(200)
})

app.get('/', (req, res) => {
  res.send('Hello from Telegram bot!')
})

app.listen(port, () => {
  console.log(`Server running on port ${port}`)
})
