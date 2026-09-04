import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()


API_ID = 21968859

API_HASH = "21a59d21687f01d448530ee88a26b1eb"

BOT_TOKEN = "7616480254:AAHlTXIbSTB_HzYC4zHsoPLgclSlIyL4l0w"

BOT_ID = 7616480254

BOT_USERNAME = "@Aethonixmusicbot"

OWNER_USERNAME = "@eren_aethonix"

BOT_NAME = "˹𝐀ᴇᴛʜᴏɴɪ𝐱 ꭙ 𝐌ᴜ𝐬ɪᴄ ˼™🎧"

ASSUSERNAME = "@Eren_playz"

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://itsiconicyt_db_user:EREN123456@eren26.eaevtp2.mongodb.net/?appName=Eren26&retryWrites=true&w=majority")

API_URL = getenv("API_URL", 'https://api.thequickearn.xyz') #youtube song url
VIDEO_API_URL = getenv("VIDEO_API_URL", 'https://api.video.thequickearn.xyz')
API_KEY = getenv("API_KEY", "30DxNexGenBots107029")

DURATION_LIMIT_MIN = 500000

LOGGER_ID = int(getenv("LOGGER_ID", "@logsaethoflix"))

DISASTER_LOG = "@logsaethoflix"

OWNER_ID = 7774827065

SPECIAL_USER = 7774827065

HEROKU_APP_NAME = "vipppp"

HEROKU_API_KEY = "HRKU-3a48d735-445f-49c4-a6cf-fea438f945ef"

UPSTREAM_REPO = "https://github.com/paradox-zenu/test"

UPSTREAM_BRANCH = "master"

GIT_TOKEN = "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"

SUPPORT_CHANNEL = "https://t.me/aethonixsupport"

SUPPORT_CHAT = "https://t.me/igrischatsupport"

AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = 9000

SPOTIFY_CLIENT_ID = "22b6125bfe224587b722d6815002db2b"

SPOTIFY_CLIENT_SECRET = "c9c63c6fbf2f467c8bc68624851e9773"

SERVER_PLAYLIST_LIMIT = 3000
PLAYLIST_FETCH_LIMIT = 25

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

SONG_DOWNLOAD_DURATION = 9999999
SONG_DOWNLOAD_DURATION_LIMIT = 9999999

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

STRING1 = getenv("STRING1", "BQFPN9sAxGVmkqq2onoCkBO5XWrtxGH3bUjpiS5DHOq79A8q5FGq1grXcxSVu8EJF29HJWD15qgqAU4B7FL2fkosIU0FxHCBcH2NT8SwXr3dvn4gNkbE_Uz3C1Gm2HORqdltQW7Zok3GWm5TPyozyHFhe6pUa24s0DX-U3E-wqbsVSk23-VX1uJZ8RKg3vZ436dsBnpXT90M4mHPoQMDYltXTySbvv-uanKKCEoTNAsch9Is_YG4itaV3lp3dGABCkCVuHM6ZO4ikhfMuNgc-V0rZb2KZ8fV-F6z9egITLbbdLLE7z7g6HBQ2Dp1Xg_4ut1XrR18dxfxsEw_yEAHOh-98787XgAAAAHYyfknAA")
STRING2 = getenv("STRING2", None)
STRING3 = getenv("STRING3", None)
STRING4 = getenv("STRING4", None)
STRING5 = getenv("STRING5", None)
STRING6 = None
STRING7 = None


filter = filters.user()
BANNED_USERS = filter
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL =  "https://i.ibb.co/rf5HWY5F/photo-2025-08-30-17-35-40-7544433638260080648.jpg"
PLAYLIST_IMG_URL = "https://i.ibb.co/rf5HWY5F/photo-2025-08-30-17-35-40-7544433638260080648.jpg"
STATS_IMG_URL = "https://i.ibb.co/rf5HWY5F/photo-2025-08-30-17-35-40-7544433638260080648.jpg"
TELEGRAM_AUDIO_URL = "https://i.ibb.co/rf5HWY5F/photo-2025-08-30-17-35-40-7544433638260080648.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/rf5HWY5F/photo-2025-08-30-17-35-40-7544433638260080648.jpg"
STREAM_IMG_URL = "https://i.ibb.co/rf5HWY5F/photo-2025-08-30-17-35-40-7544433638260080648.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/rf5HWY5F/photo-2025-08-30-17-35-40-7544433638260080648.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/rf5HWY5F/photo-2025-08-30-17-35-40-7544433638260080648.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/rf5HWY5F/photo-2025-08-30-17-35-40-7544433638260080648.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/rf5HWY5F/photo-2025-08-30-17-35-40-7544433638260080648.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/rf5HWY5F/photo-2025-08-30-17-35-40-7544433638260080648.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
