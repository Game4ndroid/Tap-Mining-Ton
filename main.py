from flask import Flask, request
import telebot
import os

API_TOKEN = os.environ.get("BOT_TOKEN")  # Gunakan env var
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Selamat datang di Ton Mining 🎯!")

@app.route(f'/{API_TOKEN}', methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return '', 200

@app.route('/')
def index():
    return "TON Mining Bot is running!"

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"{os.environ.get('WEBHOOK_URL')}/{API_TOKEN}")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
