import asyncio
import logging
import aiohttp
from aiogram import Bot, Dispatcher,F, types
from aiogram.filters.command import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, FSInputFile,KeyboardButton
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import random
import keyboard as kb


from config import TOKEN, WEATHER_API_KEY
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Включаем логирование
logging.basicConfig(level=logging.INFO)

CITY = "Moscow"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}&units=metric&lang=ru"

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Hi {message.from_user.first_name}! I am a bot!',reply_markup=kb.main_keyboard)
    # Inline Buttons :
    # await message.answer(f'Hi {message.from_user.first_name}! I am a bot!',reply_markup=kb.inline_keyboard)
    # Keyboard Builder
    # await message.answer(f'Hi {message.from_user.first_name}! I am a bot!',reply_markup=kb.test_keyboard())

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer(
        "This Bot can do :\n"
        "/start - приветствие\n"
        "/help - помощь\n"
        "/echo - повтор\n"
        "/photo - случайное фото\n"
        "/weather [город] - прогноз погоды"
    )

@dp.message(F.text == 'What is your name?')
async def text_answer(message: Message):
    await message.answer('WALL-E (Waste Allocation Load Lifter Earth-Class) , the last functioning robot on a garbage-covered Earth')

@dp.message(F.photo)
async def photo_answer(message: Message):
    list = ['Wow, what a picture!','Not Bad!','Dont send me this!','What should I do with that?']
    rand_ans = random.choice(list)
    await message.answer(rand_ans)
    await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')

@dp.message(Command('photo'))
async def photo_random(message: Message):
    list = ['https://www.freepik.com/free-photo/grey-kitty-with-monochrome-wall-her_13863400.htm#fromView=keyword&page=1&position=3&uuid=7ffedd04-878b-4649-89b2-61a5280cdcf1&query=Cat','https://www.freepik.com/free-vector/cat-paws-icon-collection_8270958.htm#fromView=keyword&page=1&position=6&uuid=7ffedd04-878b-4649-89b2-61a5280cdcf1&query=Cat']
    rand_photo = random.choice(list)
    await message.answer_photo(photo= rand_photo, caption='Random photo')

@dp.message(Command('video'))
async def video(message: Message):
    await bot.send_video(message.chat.id, 'uploading video')
    myvideo = FSInputFile('Countdown1.mp4')
    # await message.answer_video(video=myvideo)
    await bot.send_video(message.chat.id, video=myvideo)

@dp.message(Command('audio'))
async def audio(message: Message):
    await bot.send_audio(message.chat.id, 'uploading audio')
    myaudio = FSInputFile('laser_shoot.wav')
    await bot.send_audio(message.chat.id, audio=myaudio)

@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile('laser_shoot.wav')
    await message.answer_voice(voice=voice)
    # await bot.send_voice(message.chat.id, 'uploading voice')

@dp.message(Command('training'))
async def training(message: Message):
   training_list = [
       "Тренировка 1:\\n1. Скручивания: 3 подхода по 15 повторений\\n2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\\n3. Планка: 3 подхода по 30 секунд",
       "Тренировка 2:\\n1. Подъемы ног: 3 подхода по 15 повторений\\n2. Русский твист: 3 подхода по 20 повторений (каждая сторона)\\n3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
       "Тренировка 3:\\n1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\\n2. Горизонтальные ножницы: 3 подхода по 20 повторений\\n3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
   ]
   rand_tr = random.choice(training_list)
   await message.answer(f"Это ваша мини-тренировка на сегодня {rand_tr}")

   tts = gTTS(text=rand_tr, lang='ru')
   tts.save("training.ogg")
   voice = FSInputFile('training.ogg')
   # await message.answer_voice(voice=voice)
   # await bot.send_audio(message.chat.id, voice)
   await bot.send_voice(message.chat.id, voice)

   os.remove('training.ogg')

@dp.message(Command('doc'))
async def doc(message: Message):
    mydoc = FSInputFile("ZZZ.txt")
    await bot.send_document(message.chat.id,mydoc)



####### API Weather #######
@dp.message(Command('weather'))
async def weather(message: Message):
    args = message.text.split(maxsplit=1)

    if len(args) > 1:
        city = args[1]
    else:
        city = "Moscow"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                temp = data["main"]["temp"]
                description = data["weather"][0]["description"]
                await message.answer(
                    f"Погода в {city}:\n🌡 Температура: {temp}°C\n☁ {description.capitalize()}"
                )
            else:
                # Print full error response for debugging
                error_text = await resp.text()
                await message.answer(
                    f"Не удалось найти погоду для города '{city}' 😢\n"
                    f"Код ошибки: {resp.status}\nОтвет: {error_text}"
                )
############################################################################

# Словарь для хранения выбранного языка каждого пользователя
user_lang = {}

# Доступные языки
LANGUAGES = {
    "Английский 🇬🇧": "en",
    "Немецкий 🇩🇪": "de",
    "Французский 🇫🇷": "fr",
    "Испанский 🇪🇸": "es",
    "Итальянский 🇮🇹": "it",
    "Русский 🇷🇺": "ru"   # можно вернуться к русскому
}

# Клавиатура для выбора языка
def get_language_keyboard():
    buttons = [[KeyboardButton(text=lang)] for lang in LANGUAGES.keys()]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


@dp.message(Command('translate'))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! 👋 Выбери язык, на который я буду переводить твои сообщения:",
        reply_markup=get_language_keyboard()
    )
@dp.message(lambda message: message.text in LANGUAGES.keys())
async def set_language(message: types.Message):
    user_lang[message.from_user.id] = LANGUAGES[message.text]
    await message.answer(f"✅ Язык перевода установлен: {message.text}")

@dp.message()
async def translate_message(message: types.Message):
    # Skip if the message is a command or language selection
    if message.text.startswith('/') or message.text in LANGUAGES:
        return
        
    lang = user_lang.get(message.from_user.id, "en")  # Default to English
    try:
        translated_text = GoogleTranslator(source="auto", target=lang).translate(message.text)
        await message.answer(f"Перевод ({lang}):\n{translated_text}")
    except Exception as e:
        logging.exception(e)
        await message.answer("⚠️ Ошибка при переводе. Попробуйте снова.")


############################################################################
@dp.message(Command('echo'))
async def echo(message: Message):
    await message.answer(message.text)

@dp.message()
async def my_echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())