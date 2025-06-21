import axios from 'axios';

const TOKEN = process.env.BOT_TOKEN;
const TELEGRAM_API = `https://api.telegram.org/bot${TOKEN}`;

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).send('Method Not Allowed');

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

  res.status(200).end();
}