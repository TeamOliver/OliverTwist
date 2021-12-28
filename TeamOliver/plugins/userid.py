import html

@bot.on_message(filters.command('id') & filters.private)
def id(bot, message):
      message.reply_text(f"Your id is :-<code>{message.chat.id}</code>}
