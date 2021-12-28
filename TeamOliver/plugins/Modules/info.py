from pyrogram import Client, filters

@Client.on_message(filters.command("info", "whois"))
def info(_, message):
    user = message.from_user.id
    ppic_ct = bot.get_profile_photos_count(user)

    if not ppic_ct == 0:
        ppic = bot.get_profile_photos(user, limit=1)
        p_pic = ppic[0]['thumbs'][0]['file_id']

    usr = bot.get_users(user)
    info = f"""**First Name** : {foo.first_name}
**Last Name**: {usr.last_name}
**Id**: {usr.id}
**Permanent Link**: {usr.mention(message.from_user.first_name)}
**Is bot**: {usr.is_bot}
"""

    if ppic_ct != 0:
        message.reply_photo(p_pic, caption=info)
    else:
        message.reply_text(info)
