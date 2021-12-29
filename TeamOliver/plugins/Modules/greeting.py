from pyrogram import Client, filters

from TeamOliver import WELCOME_TEXT


title = message.chat.title
grp_id = message.chat.id
GROUP = "grp_id"
WELCOME_TXT = WELCOME_TEXT

@Client.on_message(filters.chat(GROUP) & filters.new_chat_members)
async def welcomebot(Client, message):
     try:
        await message.reply_text(WELCOME.TXT.format(message.from_user.first_name, title)
     except Exception as e:
        print(e)
        message.reply_text("I couldn't welcome new member")

@Client.on_message(filters.command('welcome') & filters.group)
async def showwel(Client, message):
        try:
          message.reply_text(f"The current welcome message of **{title}** is :-\n \n {WELCOME.TXT}")
        exept Exception as e:
          print(e)
          message.reply_text("something went wrong")

