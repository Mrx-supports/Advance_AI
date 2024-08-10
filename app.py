from flask import Flask, request
import os
from pyrogram import Client

app = Flask(__name__)

# Initialize your bot client
bot = Client("my_bot", bot_token=os.getenv('BOT_TOKEN'))

@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data(as_text=True)
    update = bot.parse_update(json_str)
    bot.process_update(update)
    return "ok"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
