import os
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardmarkup 
from TeamOliver.strings import START_TXT, HELP_TXT, ABOUT_TXT, IMAGES, GROUP_START_TEXT

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    await message.reply_photo(
    photo=random.choice(IMAGES),
    caption=START_TXT.format(mention=mesage.from_user.mention,
                             first=message.from_user.first_name,
                             last=message.from_user.last_name,
                             username=message.from_user.username),
    reply_markup=InlineKeyboardMarkup([[
                                      InlineKeyboardButton("➕ Add Me To Your Groups", url=f"https://t.me/{BOT_USERNAME}/start?group".format(bot_username)
                                      ],[
                                      InlineKeyboardButton("ℹ️ Help", callback_data="help"),
                                      InlineKeyboardButton("🔰 About", callback_data="about")
                                      ],[
                                      InlineKeyboardButton("Close ⛔", callback_data="close"),
                                      InlinekeyboardButton("📚 Source Code", url="https://github.com/TeamOliver/OliverTwist")
                                      ]]))

@Client.on_message(filters.command('start') & filters.group)
async def grpstart(client, message):
    await message.reply_photo(
    photo=random.choice(IMAGES),
    caption=GROUP_START_TEXT)

@Client.on_message(filters.command('about') & filters.private)
async def about(Client,message):
       await message.reply_photo(random.choice(IMAGES),
       caption=ABOUT_TXT,
    reply_markup=InlinekeyboardMarkup([
              [InlinekeyboardButton("Back", callback_data="start"]
   ])
   )
