## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAEISpMAh7UtSarEC7TZzYv9KXPwXAvyUAN-ew5LSS_boegDA_low2BLzH1ECN5O6DOutj9Sks4sD09cy7oyxkX-qPpvW9PxG15zopNzEPTto3UuF27kBY-L58SBc5pgL5gw4SB1C2SfriQLXENRfq3VRkc5jvOAlEKY_sYFZMU9SNDdojJv6WiFyHsrxo98LF4ASU3E3N0AI5SObCRL65AwewYEE5yYJc7tCrbbVJxh6tRANqttSUaHZ-0C52UtNmvljDEPL_WNgMyGhu0GmzekSmL-JdjBNcwtEI27Xq15DsdOgqKR9yCEvqoL_UvT4_QV5ZOsyVWBxANdxWHaBHCANP_ydQAAAABu0T8VAA")
BOT_TOKEN = getenv("BOT_TOKEN", "5451906359:AAHJad0ukmJFe3rKOIvEwo5ApDz_7hkogIM")
BOT_NAME = getenv("BOT_NAME", "SEAZSH_BOT")
API_ID = int(getenv("API_ID", "17320595"))
API_HASH = getenv("API_HASH", "bb0fbf90e7c8f09160608d1962200221")
OWNER_NAME = getenv("OWNER_NAME", "TTT_TTR")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@t_4lb")
ALIVE_NAME = getenv("ALIVE_NAME", "هـوس")
BOT_USERNAME = getenv("BOT_USERNAME", "SEAZSH_BOT")
OWNER_ID = getenv("OWNER_ID", "1777087402")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "TTT_TTR")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "VFF35")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "VFF35")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5383415297").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/46fa55b49b85c084159ce.png")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/466de30ee0f9383c8e09e.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
