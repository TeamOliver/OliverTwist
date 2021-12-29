from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

Button = InlineKeyboardMarkup
TGButton = InlineKeyboardButton
Data = callback_data
Link = url
BUTTONS = Button(
        [[
        TGButton(f"{FILTER_BUTTON_TEXT}", Data=f"{FILTER_BUTTON_DATA}")
        ]]
    )
        
# Button Text List       
FILTER_BUTTON_TEXT = "Filter"






# Button Data List

FILTER_BUTTON_DATA = "filter_help"
