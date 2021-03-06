import html
from pyrogram.types import InlinekeyboardButton,InlinekeyboardMarkup

from TeamOliver import BOT_TOKEN, START_IMAGE

BOT_IMAGE = START_IMAGE

temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        self.username = '@' + me.username

START_TXT = """
Hello My dear <b>{}</b>, My name is <b>{}</b>. I am a powerfull. I am a bot
which can provide movies in your group😘. I have a few extras as well.
You can check my features by hitting /help 💕.
""".format(message.from_user.first_name, me.first_name)

GROUP_START_TEXT = """
Hello {}, contact me in pm if you wanna use me 🤗
""".format(message.from_user.first_name)

WELCOME_TEXT = """
hey {}, welcome to {}. So tell us about yourself.
""".format(message.from_user.first_name, title)

ABOUT_TXT = """
Owner = <a href="t.me//user?id={}">This person</a><br>
Source-code = <a href="https://github.com/TeamOliver/OliverTwist">Click here</a><br> #fill this later
Language = Python3<br>
Database = MongoDB<br>
library = Pyrogram asyncio<br>
Creators = <a href="https://t.me/TeamOliver">TeamOliver</a> <br>#fill this later
"""

HELP_TXT = """
<b>HELP DESK OF {}</b>

- /start - check if I'm alive<br>
- /help - comes in this same page<br>
- /stats - Gives the bot stats<br>

<b>And the following </b>
""".format(me.first_name)

SLAP_TEMPLATES = (
    "{user1} {hits} {user2} with a {item}.",
    "{user1} {hits} {user2} in the face with a {item}.",
    "{user1} {hits} {user2} around a bit with a {item}.",
    "{user1} {throws} a {item} at {user2}.",
    "{user1} grabs a {item} and {throws} it at {user2}'s face.",
    "{user1} launches a {item} in {user2}'s general direction.",
    "{user1} starts slapping {user2} silly with a {item}.",
    "{user1} pins {user2} down and repeatedly {hits} them with a {item}.",
    "{user1} grabs up a {item} and {hits} {user2} with it.",
    "{user1} ties {user2} to a chair and {throws} a {item} at them.",
    "{user1} gave a friendly push to help {user2} learn to swim in lava."
)
ITEMS = (
    "cast iron skillet",
    "large trout",
    "baseball bat",
    "cricket bat",
    "wooden cane",
    "nail",
    "printer",
    "shovel",
    "CRT monitor",
    "physics textbook",
    "toaster",
    "portrait of Richard Stallman",
    "television",
    "five ton truck",
    "roll of duct tape",
    "book",
    "laptop",
    "old television",
    "sack of rocks",
    "rainbow trout",
    "rubber chicken",
    "spiked bat",
    "fire extinguisher",
    "heavy rock",
    "chunk of dirt",
    "beehive",
    "piece of rotten meat",
    "bear",
    "ton of bricks",
)

THROW = (
    "throws",
    "flings",
    "chucks",
    "hurls",
)
HIT = (
    "hits",
    "whacks",
    "slaps",
    "smacks",
    "bashes",
)

