#© TeamOliver
from pyrogram import Client, filters

from config import BOT_TOKEN, APP_ID, API_HASH
from TeamOliver import START_TXT, GROUP_START_TEXT

bot = Client(
       api_id = APP_ID,
       api_hash = API_HASH,
       bot_token = BOT_TOKEN
     )

bot.run()
