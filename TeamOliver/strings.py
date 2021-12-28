import html
from pyrogram.types import InlinekeyboardButton,InlinekeyboardMarkup

from TeamOliver import BOT_TOKEN, START_IMAGE

BOT_IMAGE = START_IMAGE

START_TXT = """
Hello My dear <b>{mention}</b>, My name is <b>{}</b>. I am a powerfull. I am a bot
which can provide movies in your group😘. I have a few extras as well.
You can check my features by hitting /help 💕.
"""

GROUP_START_TEXT = """
Hello {}, contact me in pm if you wanna use me 🤗
""".format(message.from_user.first_name)

WELCOME_TEXT = """
hey {}, welcome to {}. So tell us about yourself.
"""
ABOUT_TXT = """
Owner = <a href="t.me//user?id={}">This person</a><br>
Source-code = <a href="github.com/TeamOliver/ ">Click here</a><br> #fill this later
Language = Python3<br>
Database = MongoDB<br>
library = Pyrogram asyncio<br>
Creators = <a href="t.me/ ">TeamOliver</a> <br>#fill this later
"""

HELP_TXT = """
<b>HELP DESK OF {}</b>

- /start - check if I'm alive<br>
- /help - comes in this same page<br>
- /stats - Gives the bot stats<br>

<b>And the following </b>
"""


