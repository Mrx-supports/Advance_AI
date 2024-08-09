from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
from datetime import datetime
import os
import asyncio
from aiohttp import web

# Fetch environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')

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
    # Fetch user details
    user = update.effective_user
    user_name = user.first_name if user.first_name else "User"
    user_id = user.id
    user_mention = user.mention_html()  # For HTML formatted mention
    username = user.username if user.username else "NoUsername"
    
    # Get bot's name
    bot_name = context.bot.name
    
    # Determine Mr. or Mrs. based on the first letter of the username
    title = "Mr." if user_name[0].lower() < 'n' else "Mrs."

    # Get the appropriate greeting
    greeting = get_greeting()
    
    # Monospace formatted start message with the user's name, username, and ID
    start_message = (
        f"𝙷𝚎𝚕𝚕𝚘 {title} {user_mention}! {greeting}!\n\n"
        f"🔍 𝚈𝚘𝚞𝚛 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝙳𝚎𝚝𝚊𝚒𝚕𝚜:\n"
        f"• 𝙽𝚊𝚖𝚎: {user_name}\n"
        f"• 𝚄𝚜𝚎𝚛𝚗𝚎: @{username}\n"
        f"• 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝙸𝙳: `{user_id}`\n\n"
        f"𝙼𝚢 𝚗𝚊𝚖𝚎 𝚒𝚜 {bot_name}.\n"
        "𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 ᴀɪ ᴅᴇᴛᴀɪʟꜱ, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍\n"
        "How can I help you today?"
    )

    # Define inline buttons with the desired font and links
    keyboard = [
        [
            InlineKeyboardButton("ꜱᴜᴩᴩᴏʀᴛ ɢʀᴏᴜᴩ", url='https://t.me/MRXSUPPORTS'),
            InlineKeyboardButton("ꜱᴜᴩᴩᴏʀᴛ ɢʀᴏᴜᴩ 2.0", url='https://t.me/XBOTSUPPORTS'),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the start message with buttons and photo
    await update.message.reply_photo(
        photo="https://graph.org/file/d152a563023ea62f9ccfd.jpg",
        caption=start_message,
        parse_mode='HTML',
        reply_markup=reply_markup
    )

# Function to run both the bot and aiohttp server
async def main():
    # Start the Telegram bot
    bot_application = Application.builder().token(BOT_TOKEN).build()
    bot_application.add_handler(CommandHandler("start", start))
    
    # Start the aiohttp server
    aiohttp_app = web.Application()
    aiohttp_app.add_routes([
        web.get("/", root_route_handler)
    ])
    runner = web.AppRunner(aiohttp_app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)  # Adjust the port if necessary
    await site.start()

    # Run the bot polling in the current event loop
    await bot_application.initialize()
    asyncio.create_task(bot_application.run_polling())

    # Keep the process running
    while True:
        await asyncio.sleep(3600)  # Sleep for 1 hour

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
