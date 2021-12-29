from pyrogram.types import ChatPermission
from pyrogram import Client, filters

from TeamOliver import ADMIN_LIST

async def admins(client, message):
    x = await client.get_chat_member(message.chat.id, message.from_user.id)
    if x.status == ("administrator" or "creator"):
        return True
    else:
        return False

@Client.on_message(filters.command('ban') & filters.group)
async def ban(Client, message):
      if not admins:
          return
      else:
          if message.reply_to_message.from_user.id in ADMIN_LIST :
              message.reply_text("He is in my adminlist. I can't ban him")
          else:
             try:
                 Client.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
                 message.reply_text(f"{message.reply_to_message.from_user.first_name} has been banned.")
             except Exception as e:
                print(e)
                message.reply_text("something went wrong")
 
