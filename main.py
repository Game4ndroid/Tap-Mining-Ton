from flask import Flask, request
import telegram
import os

TOKEN = os.getenv("BOT_TOKEN", "1898020009:AAF28cW1GjDOsWil5Zg_FFlMiqIuXYIWn6Y")
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route(f"/1898020009:AAF28cW1GjDOsWil5Zg_FFlMiqIuXYIWn6Y", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    if text == "/start":
        bot.send_message(chat_id=chat_id, text="🎯 Selamat datang di Ton Mining!\n\nGabung ke channel & grup:\n📣 @Game4ndro\n👥 @Game4ndroit\n\nMining akan dimulai otomatis... 💎")
    else:
        bot.send_message(chat_id=chat_id, text="⚠️ Perintah tidak dikenal.")

    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "Bot Ton Mining aktif!"

if __name__ == "__main__":
    app.run()
