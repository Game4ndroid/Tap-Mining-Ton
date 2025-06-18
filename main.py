from flask import Flask, request
import telebot

# Langsung pakai token dan webhook URL
API_TOKEN = "1898020009:AAF28cW1GjDOsWil5Zg_FFlMiqIuXYIWn6Y"
WEBHOOK_URL = "https://ton-mining.up.railway.app"  # Ganti dengan URL Railway kamu

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Selamat datang di Ton Mining 🎯!\n\nGabung channel @Gamge4ndro & grup @Game4ndroit dulu ya!")

@app.route(f'/{API_TOKEN}', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return '', 200

@app.route('/')
def index():
    return "TON Mining Bot is running!"

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"{WEBHOOK_URL}/{API_TOKEN}")
    app.run(host="0.0.0.0", port=5000)
    
