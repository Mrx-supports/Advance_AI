import requests
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram import Client, filters
import httpx


@Client.on_message(filters.command(["openai", "gpt", "gpt4"]))
async def openaiprochatgpt(_: Client, message: Message):    
    user_id = message.from_user.id    
    if len(message.command) < 2:
        return await message.reply_text("Give An Input !!")
        
    text = " ".join(message.command[1:])    
    msg = await message.reply_text("⏳")
    url = f"https://horrid-api.onrender.com/gpt?query={text}"    
    try:
         response = requests.get(url)
         results = response.json()
         res = results["text"][0]["response"]
         
         await msg.edit(f"ʜᴇʏ: {message.from_user.mention}\n\nϙᴜᴇʀʏ: {text}\n\nʀᴇsᴜʟᴛ:\n\n{res}")
    except requests.exceptions.RequestException as e:
         print(e)
         await msg.edit(f"An error occurred: {e}")    

@Client.on_message(filters.command(["bard", "gemini", "bardai", "geminiai"]))
async def bardandgemini(_: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Give An Input!!")

    query = " ".join(message.command[1:])    
    txt = await message.reply_text("⏳")
    app = f"https://horrid-api.onrender.com/bard?query={query}"
    response = requests.get(app)
    data = response.json()
    api = data['text']
    await txt.edit(f"ʜᴇʏ: {message.from_user.mention}\n\nϙᴜᴇʀʏ: {query}\n\nʀᴇsᴜʟᴛ:\n\n{api}")
