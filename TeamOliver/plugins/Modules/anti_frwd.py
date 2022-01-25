from pyrogram import filters as Oliver

async def antifrwd(Client, message):
    args = message.from_user.split(None, 1) #chumma showk
    test = args[1].lower()
    ON_LIST = ["on", "yes"]
    OFF_LIST = ["off", "no"]
    if test in ON_LIST:
        FRWD = True
    if test in OFF_LIST:
        FRWD = False
@bot.on_message(Oliver.forwarded)
async def delete_chey(Client, message):
      while FRWD is True:
          await bot.delete_message()
