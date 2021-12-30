from pyrogram import Client, filters

from TeamOliver.strings import WELCOME_TEXT


title = message.chat.title
grp_id = message.chat.id
GROUP = "grp_id"
WELCOME_TXT = WELCOME_TEXT

@Client.on_message(filters.chat(GROUP) & filters.new_chat_members)
async def welcomebot(Client, message):
     try:
        await message.reply_text(WELCOME.TXT)
     except Exception as e:
        print(e)
        message.reply_text("I couldn't welcome new member")

@Client.on_message(filters.command('welcome') & filters.group)
async def showwel(Client, message):
        try:
          message.reply_text(f"The current welcome message of **{title}** is :-\n \n {WELCOME.TXT}")
        except Exception as e:
          print(e)
          message.reply_text("something went wrong")

@Client.on_message(filters.command('setwelcome') & filters.group)
async def setwel(Client, message):
       if message.reply_to_message:
         try:
             WELCOME_TXT = message.reply_to_message
             await message.reply_text(f"New welcome message set for **{title}**")
         except exception as e:
             print(f"faild to set welcome message for {title}. Error occurred :- {e}")
       else:
          args = message.from_user.split(None, 1)
          if len(args) >= 2:
             WELCOME_TXT = args[1]
          else:
             message.reply_text("You haven't given the welcome message")
