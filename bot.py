import pyrogram, random, time
from pyrogram import Client, filters

api_id = 123456
api_hash = "abcdef"
SETTINGS_BOT_TOKEN = "token"

bot = Client("nana", api_id=api_id, api_hash=api_hash, bot_token=SETTINGS_BOT_TOKEN)

class Error(Exception):
	pass

@bot.on_message(filters.command(["start"]))
async def start(client, message):
	await message.reply("Start successfully!")

@bot.on_message(filters.command(["help"]))
async def help(client, message):
	await message.reply("Here is a tips from me @AyraHikari")
	await message.reply("You can add command list at @BotFather")
	await message.reply("With add /setting or /help will bring new menu called 'Settings' or 'Help' in bot PM")
	await message.reply("Give a try!")
	raise Error("You ask about help?")

@bot.on_message(filters.command(["random"]))
async def random(client, message):
	ran = random.randint(1, 100)
	await message.reply("Here is a random number: " + ran)
	raise Error(ran)

@app.on_message(Filters.command(["ping"]))
async def ping(client, message):
	start_time = time.time()
	await message.edit("🏓 Pong!")
	end_time = time.time()
	ping_time = float(end_time - start_time)
	await message.edit("🏓 Pong!\n⏱ Speed was : {0:.2f}s".format(round(ping_time, 2) % 60))

bot.run()
