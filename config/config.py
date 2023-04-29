import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

API_ID = int(getenv("API_ID", "27576230"))
API_HASH = getenv("API_HASH", "d4d7a22ca59b91766cb48441048581bd")
BOT_TOKEN = getenv("BOT_TOKEN", "5866302926:AAERb6nyW6sOJPMP9A2zclhJn90x9TPkHvQ")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "BAC1T69YLWJr5cqI56YZ6IgHsIp-ubMh9m797r_2wXGMwqXRQdygeaWrsN8bSB9sibDCsg10OXOZ-hYBVcuA1hO6E3fRbOPTDUbltT162xhjCa_5wDM0yBGVSoEcneCZB74Y1d2tMdAOhBGLUTgc6FWT1UHJn-CCnqEVwuYZWzWZhl6xBG0uJX0u0oAx6cQC3pHbBK58jasZ2nEvFcRYR8JvcFOPElx8YzyVLNGR1Ip_B_nuOdGSHAuMzRW0Dfcu5E2UgSVYEEy11yD2XtsytFuXhkZksgjQLxXUAokfZY3D-3JIMwkSmI5CNGn_Pbk6eE0LvORymG_k6N63z8l2KJvcAAAAAXS7y9wA")
BOT_USERNAME = getenv("BOT_USERNAME", "K0HBOT")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5676384368").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-883778233")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "https://t.me/NO1BROS")
GROUP = getenv("GROUP", "https://t.me/NO1BROS")
BOT_NAME = getenv("BOT_NAME", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


