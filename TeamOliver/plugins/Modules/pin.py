from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("pin") & filters.group)
async def pin(client, message):
    try:
        message_id = message.reply_to_message.message_id
        await client.pin_chat_message(message.chat.id, message_id)
        await message.edit("<code>Pinned successfully!</code>")
    except:
        await message.edit("Reply to the message you want to pin")

# Need to add unpin function
