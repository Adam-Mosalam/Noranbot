from flask import Flask, request
import telegram
import os

TOKEN = "7866714715:AAGPmEyTYcH4bawsLwTpQxHHqysGEVs_Mf0"
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return "Noran Bot is alive!"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    message = update.message.text

    reply = f"أهلًا بك في بوت نوران، أرسلت: {message}"
    bot.sendMessage(chat_id=chat_id, text=reply)

    return "ok"

if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=PORT)
