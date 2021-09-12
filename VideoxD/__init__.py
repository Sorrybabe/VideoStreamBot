from misc import app, bot, HELP, Calls
from config import VIDEO_CHAT_ID 
chat_id = VIDEO_CHAT_ID

print("[LOG] Starting Client Temporarily for Information")
bot.start()
client = bot.get_me()
BOT_ID = client.id
BOT_NAME = client.first_name
BOT_USERNAME = client.username
print(BOT_USERNAME)
print("[LOG] Loaded Information")
bot.stop()
