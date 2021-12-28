#© TeamOliver
from pyrogram import Client, filters

from TeamOliver import BOT_TOKEN, API_ID, API, HASH
from TeamOliver import START_TXT, GROUP_START_TEXT

bot = Client(
       api_id = API_ID,
       api_hash = API_HASH,
       bot_token = BOT_TOKEN
     )

bot.run()
