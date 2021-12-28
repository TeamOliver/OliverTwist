import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardmarkup 
import random
from plugins.strings import START_TXT, HELP_TXT, ABOUT_TXT

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    await message.reply_text(
    text=START_TXT.format(mesage.from_user.mention),
    reply_markup=InlineKeyboardMarkup(
    [[
    InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs", url="https://t.me/{bot_username}/start?group"),
    InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help")
    ],[
    InlineKeyboardButton("ᴀʙᴏᴜᴛ ᴍᴇ", callback_data="about")
    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")
    ]])
    
