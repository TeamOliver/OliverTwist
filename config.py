import os
from os import environ

# vars that need to run the bot
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# command handle
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")
