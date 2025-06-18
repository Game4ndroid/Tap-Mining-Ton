from flask import Flask, request
import requests

app = Flask(__name__)
TOKEN = '1898020009:AAF28cW1GjDOsWil5Zg_FFlMiqIuXYIWn6Y'

@app.route(f"/1898020009:AAF28cW1GjDOsWil5Zg_FFlMiqIuXYIWn6Y", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        reply = "Selamat datang di Tap Mining TON 🎯"
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": chat_id, "text": reply})
    return {"ok": True}

@app.route("/")
def home():
    return "Bot aktif!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
