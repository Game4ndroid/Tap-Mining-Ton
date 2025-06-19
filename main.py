import telebot
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.reply_to(message, "👋 Selamat datang di Get Ton 🎯!\nKlik '🚀 Mulai Mining' untuk memulai.")

print("Bot aktif menggunakan polling di Fly.io...")
bot.infinity_polling()
