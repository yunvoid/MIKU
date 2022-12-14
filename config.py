import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQDGTRlEi126Oi5APoKSRawxMrNmcALWHKCj4ztrrEZEJQJdpyXj
BOT_NAME = getenv("BOT_NAME", "Miku Music")
API_ID = int(getenv("API_ID", "15476951"))
API_HASH = getenv("API_HASH", "63d22e4b2fda")
OWNER_NAME = getenv("OWNER_NAME", "Yun")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Mr_nack_nack")
ALIVE_NAME = getenv("ALIVE_NAME", "Miku Music")
BOT_USERNAME = getenv("BOT_USERNAME", "miku_mc_bot")
OWNER_ID = getenv("OWNER_ID", "5001899507")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Miku 【V๏ɪ፝֟𝔡】")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Miku_Support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Miku_updates")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "Mikumcbot")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "c56dc798-186c-4d90-b656-f2f02ec31e15")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5001899507").split()))
LOG_GRP = getenv("LOG_GRP", "-1001299748978")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROJECT_NAME = getenv("PROJECT_NAME", "MIKU")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/1460234d4ab99e311e3c0.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/de91427fe131a0578cfb4.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/de91427fe131a0578cfb4.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Yunxvoid/MIKU")
ARQ_API_KEY = getenv("ARQ_API_KEY", "GGGQSV-IOXGYR-PBLICM-QFNQIY-ARQ") 
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/100b3e9f1c6fd5c360009.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/99759e89c31a3fe414dd9.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/8f2f9b83e4420dd2f3cca.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/41a53b4571a0b90b2fd5c.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/4b767e04d236fec02ca55.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/41a53b4571a0b90b2fd5c.jpg")
