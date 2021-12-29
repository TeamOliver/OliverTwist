from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

Button = InlineKeyboardMarkup
TGButton = InlineKeyboardButton
Data = callback_data
Link = url
BUTTONS = Button(
        [[
        TGButton("Filter", Data="filter_help")
        ]]
    )
        
        
