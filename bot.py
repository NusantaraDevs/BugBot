import pyrogram
from pyrogram import Client, filters

api_id = 123456
api_hash = "abcdef"
SETTINGS_BOT_TOKEN = "token"

bot = Client("nana", api_id=api_id, api_hash=api_hash, bot_token=SETTINGS_BOT_TOKEN)

@bot.on_message(filters.command(["start"]))
async def start(client, message):
	await message.reply("Start successfully!")

@bot.on_message(filters.command(["help"]))
async def help(client, message):
	await message.reply("Here is a tips from me @AyraHikari")
	await message.reply("You can add command list at @BotFather")
	await message.reply("With add /setting or /help will bring new menu called 'Settings' or 'Help' in bot PM")
	await message.reply("Give a try!")

bot.run()
