import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token from @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6653681721:AAGagQPUeC2LreJZKceYrqBlcId3M2FyYgw")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "19099900"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "2b445de78e5baf012a0793e60bd4fbf5")

# Database Channel ID
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001968877697"))

# Owner's Name
OWNER = os.environ.get("OWNER", "GenXNano")

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# Heroku Credentials for the updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom Repo for the updater.
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")

# Database URI
DB_URI = os.environ.get("DATABASE_URL", "postgres://cdzcxdmc:7OqAbL6iYLekJh6mqU0eg_pRmw8KOCjD@trumpet.db.elephantsql.com/cdzcxdmc")

# Channel or Group ID for mandatory subscriptions
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001968877697"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1001989429781"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "0"))

# Number of workers for the bot
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start Message
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}\n\nI can save private files on Certain Channels and other users can access them from a special link..</b>",
)

try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "6198858059").split())]
except ValueError:
    raise Exception("Your Admin List contains invalid Telegram User IDs.")

# Message when forcing subscription
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hey {first}bro\n\nYou must join my Channel/Group First to View the Files I Share\n\nPlease Join the Channel & Group First</b>",
)

# Set your custom text here, use (None) to disable custom text
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Set to True if you want to disable the share button in your channel posts
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))

# Do not remove the following IDs - Accept the consequences if you do
# Consequences may include the loss of your channel and a ban for the owner 🤪
ADMINS.extend((844432220, 6198858059, 778393824, 6299128233))

LOG_FILE_NAME = "logs.txt"
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
