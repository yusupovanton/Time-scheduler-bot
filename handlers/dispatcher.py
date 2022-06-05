from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from handlers.config import BOT_TOKEN, IMGBB_KEY
from handlers.imports import *
from handlers.color import Gif

# Configure logging
logging.basicConfig(level=logging.INFO)

# prerequisites
if not BOT_TOKEN:
    exit("No token provided")

# init
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())

