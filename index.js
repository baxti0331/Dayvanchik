const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

const TOKEN = process.env.BOT_TOKEN;
const TELEGRAM_API = `https://api.telegram.org/bot${TOKEN}`;

app.post(`/webhook/${TOKEN}`, async (req, res) => {
  const update = req.body;

  try {
    if (update.message && update.message.text) {
      const chatId = update.message.chat.id;
      const text = update.message.text;

      if (text === '/start') {
        await axios.post(`${TELEGRAM_API}/sendMessage`, {
          chat_id: chatId,
          text: '👋 Привет! Бот работает через webhook 🚀',
        });
      }
    }
  } catch (error) {
    console.error('Ошибка при обработке сообщения:', error.message);
  }

  // Подтверждаем Telegram, что запрос принят
  res.sendStatus(200);
});

const port = process.env.PORT || 4000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});