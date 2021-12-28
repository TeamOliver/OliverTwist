from pyrogram.types import ChatPermission

from TeamOliver import ADMIN_LIST


@Client.on_message(filters.command('ban') & filters.group)
async def ban(Client, message):
      if message.reply_to_message.from_user.id in ADMIN_LIST :
           message.reply_text("He is in my adminlist. I cant ban him")
      else:
           try:
               bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.mention)
               message.reply_text(f"{message.reply_to_message.from_user.first_name} has been banned.")
            except Exception as e:
               print(e)
               message.reply_text("something went wrong")
