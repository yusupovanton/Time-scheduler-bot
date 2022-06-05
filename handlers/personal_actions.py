import asyncio

from handlers.dispatcher import *
from handlers.hashfuncs import reg_dict, hash_encode, create_new_pass

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
storage = MemoryStorage()


class Form(StatesGroup):
    file_choice = State()  # Will be represented in storage as 'Form:choice_command'


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


@dp.message_handler(state=None)
async def check_pwd_input(message: types.Message, state: FSMContext):
    _id_ = str(message.from_user.id)
    _hsh_ = hash_encode(st=message.text, prs=_id_)

    if reg_dict[_id_] == _hsh_:
        await Form.file_choice.set()
        chat_id_ = message.chat.id
        await message.reply(text="Choose a file from the list of files available to you:")
        path_to_usr_folder = f"handlers/users/{_id_}"

        if os.path.exists(path_to_usr_folder):
            list_of_files = os.listdir(path_to_usr_folder)
            string_of_files = "\n".join(list_of_files)
            await bot.send_message(chat_id=chat_id_, text=string_of_files, parse_mode='markdown')

        else:
            await bot.send_message(chat_id=chat_id_, text=f"No files available", parse_mode='markdown')

    else:
        print('ERROR: WRONG USER/PASS')


@dp.message_handler(state=Form.file_choice)
async def send_file(message: types.Message, state: FSMContext):

    _id_ = str(message.from_user.id)
    path_to_usr_folder = f"handlers/users/{str(_id_)}"
    fn = message.text
    chat_id_ = message.chat.id

    if message.text in os.listdir(path_to_usr_folder):
        await state.finish()
        file = f'{path_to_usr_folder}/{fn}'
        with open(file, 'r') as file_to_send:
            await bot.send_document(chat_id=chat_id_, document=file_to_send)
        new_pass = create_new_pass(_id_)
        reply = f'Your new password is above. Please save it as the password will self-destruct in 1 minute.'

        await bot.send_message(chat_id=chat_id_, text=f"{new_pass}")

        await bot.send_message(chat_id=chat_id_, text=str(reply), parse_mode='markdown')

        await asyncio.sleep(60)
        await bot.delete_message(chat_id=chat_id_, message_id=message.message_id+2)

    else:
        await bot.send_message(chat_id=chat_id_, text="No such file exists. Please check spelling", parse_mode='markdown')


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



