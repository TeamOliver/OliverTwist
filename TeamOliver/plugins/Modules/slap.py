from pyrogram import Client, filters

from TeamOliver import SLAP_TEMPLATES, ITEMS, THROW, HIT

@Client.on_message(filters.command('slap') & filters.private & filters.group)
async def slap(Client, message)
   if message.reply_to_message:
      user2= message.reply_to_message.from_user.first_name
      user2 = message.from_user.first_name
      item = random.choice(ITEMS)
      hit = random.choice(HIT)
      throw = random.choice(THROW)
      await message.reply_text(random.choice(SLAP.TEMPLATES)
   else:
      message.reply_text(f"You haven't mentioned whom to slap, So i will slap you with {item}")
