from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/bf668acd666ec26038aed.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/202ba4e6f0733c58b6e2d.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/eng_hindi_chat_group")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/UNIQUE_DPZ_COUPLES")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/19945c5e16067fd714338.jpg"

 
