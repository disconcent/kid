# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5980733791:AAFglxbnSbgqp50LMvMWTem1c4t4Q10xXe0")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "11381402"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "349d6f6868d82dc82c7a9b356051f035")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001734237214"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "nocturnalonebeing")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://vwlngvty:2ipU8-EnwDvX2mMh0sCLghTjXmQjy2v7@tuffi.db.elephantsql.com/vwlngvty")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "AbingProject")
GROUP = os.environ.get("GROUP", "AbingSupport")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001685975866"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001860869289"))
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1001893970033"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1483593900 5162360770 5721720953 5606994237").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hallo {first}\n\nSelamat datang dan jangan lupa join\n\nSilakan Join Terlebih Dahulu.. Kalau Sudah Silahkan Menikmati</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(1337194042)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
