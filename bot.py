import pyrogram
from pyrogram import Client, filters

api_id = 123456
api_hash = "abcdef"
SETTINGS_BOT_TOKEN = "token"

bot = Client("nana", api_id=api_id, api_hash=api_hash, bot_token=SETTINGS_BOT_TOKEN)

@bot.on_message(filters.command(["start"]))
async def start(client, message):
	await message.reply("Start successfully!")

bot.run()
