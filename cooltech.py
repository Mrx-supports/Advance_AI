from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
from datetime import datetime
import os

# Import settings from info.py
from info import BOT_TOKEN

# Function to get the appropriate greeting based on the current time
def get_greeting():
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 17:
        return "Good Afternoon"
    elif 17 <= current_hour < 21:
        return "Good Evening"
    else:
        return "Good Night"

# Define the /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    user_name = user.first_name if user.first_name else "User"
    user_id = user.id
    user_mention = user.mention_html()
    username = user.username if user.username else "NoUsername"
    bot_name = context.bot.name
    title = "Mr." if user_name[0].lower() < 'n' else "Mrs."
    greeting = get_greeting()

    start_message = (
        f"𝙷𝚎𝚕𝚕𝚘 {title} {user_mention}! {greeting}!\n\n"
        f"🔍 𝚈𝚘𝚞𝚛 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚍𝚒𝚝𝚎 𝙳𝚎𝚝𝚒𝚕𝚜:\n"
        f"• 𝙽𝚊𝚍𝚒𝚝𝚎: {user_name}\n"
        f"• 𝚄𝚜𝚎𝚛𝚟𝚎: @{username}\n"
        f"• 𝚃𝚎𝚕𝚎𝚐𝚛𝚨𝚽: `{user_id}`\n\n"
        f"𝙼𝚢 𝚋𝚘𝚝 𝚗𝚊𝚖𝚎 𝚒𝚜 {bot_name}.\n"
        "𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 ᴀɪ ᴅᴇᴛᴀɪʟꜱ, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚸𝙾𝚄𝚽 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝣸 😍\n"
        "How can I help you today?"
    )

    keyboard = [
        [
            InlineKeyboardButton("ꜱᴜᴩᴩᴏʀᴛ ɢʀᴏᴜᴩ", url='https://t.me/MRXSUPPORTS'),
            InlineKeyboardButton("ꜱᴜᴩᴩᴏʀᴛ ɢʀᴏᴜᴩ 2.0", url='https://t.me/XBOTSUPPORTS'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo="https://graph.org/file/d152a563023ea62f9ccfd.jpg",
        caption=start_message,
        parse_mode='HTML',
        reply_markup=reply_markup
    )

def main():
    # Use BOT_TOKEN from info.py
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    # Use PORT environment variable or default to 8080
    port = os.getenv('PORT', 8080)

    # Run the bot with polling
    application.run_polling(allowed_updates=["message", "edited_message", "callback_query"])

if __name__ == '__main__':
    main()
