import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardmarkup 
import random
from plugins.string import START_TXT, HELP_TXT, ABOUT_TXT

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    await message.reply_text(
    text=script.START_TXT.format(mesage.from_user.mention),
    reply_markup=InlineKeyboardMarkup(
    [[
    InlineKeyboardButton("➕ Add me to your groups", url="https://t.me/{bot_username}/start?group"),
    InlineKeyboardButton("🤔 Help", callback_data="help")
    ],[
    InlineKeyboardButton("🙂 About", callback_data="about")
    InlineKeyboardButton("❌ Close", callback_data="close")
    ]])
    
