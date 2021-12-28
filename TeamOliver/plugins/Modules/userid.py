from pyrogram import Client, filters

@Client.on_message(filters.command('id'))
async def id(bot, message):
    if message.reply_to_message:
          await message.reply(f"<b>{message.reply_to_message.from_user.mention}'s ID:</b> <code>{message.reply_to_message.from_user.id}</code>")
    else:
         await message.reply_text(f"<b>{message.from_user.mention("Your")} ID:</b> <code>{message.from_user.id}</code>}")
