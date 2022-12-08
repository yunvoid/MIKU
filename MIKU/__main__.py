import requests
from pyrogram import Client as Bot

from MIKU.config import API_HASH
from MIKU.config import API_ID
from MIKU.config import BG_IMAGE
from MIKU.config import BOT_TOKEN
from MIKU.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="MIKU.Player"),
)

bot.start()
run()
