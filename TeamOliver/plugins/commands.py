import os
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardmarkup 
from plugins.strings import START_TXT, HELP_TXT, ABOUT_TXT, IMAGES, GROUP_START_TEXT

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    await message.reply_photo(random.choice(IMAGES),
    caption=START_TXT.format(mention=mesage.from_user.mention,
                             first=message.from_user.first_name,
                             last=message.from_user.last_name
                             username=message.from_user.username),
    reply_markup=InlineKeyboardMarkup([
                                       [InlineKeyboardButton("➕ Add me to your groups", url="https://t.me/{bot_username}/start?group".format(bot_username),
                                        InlineKeyboardButton("❓️ Help", callback_data="help")],
                                       [InlineKeyboardButton("🙂 About", callback_data="about")
                                        InlineKeyboardButton("❌ Close", callback_data="close")]
                                     ])
                              )
@Client.on_message(filters.command('start') & filters.group)
async def grpstart(client, message):
    await message.reply_photo(random.choice(IMAGES),
    caption=GROUP_START_TEXT

