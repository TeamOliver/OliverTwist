from TeamOliver import ADMIN_LIST

USER_ID = message.from_user.id
@Client.on_message(filters.command('leave') & filters.group)
async def leave(client, message)
     if USER_ID in ADMIN_LIST :
          try:
            message.reply_text("Bye, I am leaving this chat")
            client.leave_chat(.message.chat.id)
          except exception as e:
            print(e)
            message.reply_text("something went wrong")
     else:
         print("Wait a minute, who are you..? ")

@Client.on_message(filters.command('leave') & filters.private)
async def pmleave(client, message)
     message.reply_message("This can only be used in a group")
