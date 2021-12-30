from pyrogram import Client, filters


@Client.on_message(filters.command("del") & filters.group)
async def del_message(client, message):
    member = await client.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    if member.can_delete_messages:
       try:
           await message.reply_to_message.delete()
       except Exception as e:
           await message.reply("I can't delete that message")
           print(e)
       try:
           await message.delete()
       except Exception as e:
           print(e)
    else:
         await message.reply("You don't have permission to do this!")
