import base64
from uuid import uuid4
import requests as requests
from aiogram import types, md
from dispatcher import dp
from color import *
from config import BOT_TOKEN, CHANNEL_ID, INVEST_BOT, IMGBB_KEY
import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle

API_TOKEN = BOT_TOKEN

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)


def cache_photo(text):
    id_ = random.randint(0, 1000)
    file_name = Gif(text).method2()

    with open(file_name, "rb") as file:
        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": IMGBB_KEY,
            "image": base64.b64encode(file.read()),
        }
        response = requests.post(url, payload)
        if response.status_code == 200:
            return {"photo_url": response.json()["data"]["url"], "thumb_url": response.json()["data"]["thumb"]["url"]}

    return None


@dp.message_handler()
async def check_language(message: types.Message):
    locale = message.from_user.locale

    await message.reply(md.text(
        md.bold('Info about your language:'),
        md.text('🔸', md.bold('Code:'), md.code(locale.language)),
        md.text('🔸', md.bold('Territory:'), md.code(locale.territory or 'Unknown')),
        md.text('🔸', md.bold('Language name:'), md.code(locale.language_name)),
        md.text('🔸', md.bold('English language name:'), md.code(locale.english_name)),
        sep='\n',
    ))


@dp.inline_handler()
async def inline_gifify(inline_query: InlineQuery):

    text = inline_query.query
    upphoto = cache_photo(text)
    with open('background.png', 'r') as photo:

        item = InlineQueryResultArticle(
                        id=str(uuid4()),
                        title="Your Gif",
                        thumb_url=upphoto['thumb_url'],
                        url=upphoto['photo_url'],
                        input_message_content=InputTextMessageContent(upphoto['photo_url'])
        )
    # don't forget to set cache_time=1 for testing (default is 300s or 5m)
    await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)



