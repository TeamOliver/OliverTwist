from pyrogram import Client, filters

@Client.on_message(filters.command('id'))
async def id(bot, message):
    await message.reply_text(f"Your id is :-<code>{message.from_user.id}</code>}")
