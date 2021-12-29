from pyrogram import Client, filters
from TeamOliver import ADMIN_LIST


@Client.on_message(filters.command('leave'))
async def leave(client, message):
     if message.chat.type = "private":
          await message.reply("This can only be used in a group")
     else:
          if message.from_user.id in ADMIN_LIST :
               try:
                  await message.reply_text("Bye, I am leaving this chat")
                  await client.leave_chat(message.chat.id)
               except Exception as e:
                  print(e)
                  await message.reply_text("something went wrong")
          else:
              await message.reply("Wait a minute, who are you..?")
     

     
