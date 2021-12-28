from pyrogram import Client, filters
import os
from pyrogram.types import Message



@Client.on_message(filters.command("del"))
async def del_message(c, m):
    try:
        await client.delete_messages(message.chat.id, message.reply_to_message.message_id)
    except RPCError as e:
        print(e)
    try:
        await client.delete_messages(message.chat.id, message.message_id)
    except RPCError as e:
        print(e)
