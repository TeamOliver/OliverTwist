from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

Button = InlineKeyboardMarkup
TGButton = InlineKeyboardButton
Data = callback_data
Link = url
BUTTONS = Button(
        [[
        TGButton(f"{FILTER_BUTTON_TEXT}", Data="filter_help")
        ]]
    )
        
        
FILTER_BUTTON_TEXT = "Filter"
