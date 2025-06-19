import telebot
from telebot import types
import os
from datetime import datetime, timedelta

# Ambil token langsung dari environment
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Data user disimpan sementara di RAM
user_data = {}

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    user_data.setdefault(user_id, {'saldo': 0.0, 'last_mine': datetime.min})

    markup = types.InlineKeyboardMarkup()
    btn_mine = types.InlineKeyboardButton("🚀 Mulai Mining", callback_data='mine')
    markup.add(btn_mine)

    bot.send_message(
        message.chat.id,
        "👋 Selamat datang di *Get Ton Mining 🎯!*\n\nKlik tombol di bawah untuk mulai mining.",
        reply_markup=markup,
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: call.data == 'mine')
def handle_mining(call):
    user_id = call.from_user.id
    now = datetime.now()

    if user_id not in user_data:
        user_data[user_id] = {'saldo': 0.0, 'last_mine': datetime.min}

    last_mine = user_data[user_id]['last_mine']
    cooldown = timedelta(minutes=1)

    if now - last_mine >= cooldown:
        user_data[user_id]['last_mine'] = now
        user_data[user_id]['saldo'] += 0.001

        bot.answer_callback_query(call.id, "✅ Mining berhasil! +0.001 TON")
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"✅ Mining berhasil!\n\n💰 Saldo kamu: *{user_data[user_id]['saldo']:.3f}* TON",
            parse_mode="Markdown"
        )
    else:
        wait = int((cooldown - (now - last_mine)).total_seconds())
        bot.answer_callback_query(call.id, f"⏳ Tunggu {wait} detik lagi.")

print("🤖 Bot mining aktif (polling)...")
bot.infinity_polling()
