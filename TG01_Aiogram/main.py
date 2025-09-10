import asyncio
import logging
import aiohttp
from aiogram import Bot, Dispatcher,F
from aiogram.filters.command import CommandStart, Command
from aiogram.types import Message

import random

from config import TOKEN, WEATHER_API_KEY
bot = Bot(token=TOKEN)
dp = Dispatcher()


CITY = "Moscow"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}&units=metric&lang=ru"

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Hi! I am a bot!')

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

@dp.message(Command('echo'))
async def echo(message: Message):
    await message.answer(message.text)

@dp.message(F.text == 'What is your name?')
async def text_answer(message: Message):
    await message.answer('WALL-E (Waste Allocation Load Lifter Earth-Class) , the last functioning robot on a garbage-covered Earth')

@dp.message(F.photo)
async def photo_answer(message: Message):
    list = ['Wow, what a picture!','Not Bad!','Dont send me this!','What should I do with that?']
    rand_ans = random.choice(list)
    await message.answer(rand_ans)

@dp.message(Command('photo'))
async def photo_random(message: Message):
    list = ['https://www.freepik.com/free-photo/grey-kitty-with-monochrome-wall-her_13863400.htm#fromView=keyword&page=1&position=3&uuid=7ffedd04-878b-4649-89b2-61a5280cdcf1&query=Cat','https://www.freepik.com/free-vector/cat-paws-icon-collection_8270958.htm#fromView=keyword&page=1&position=6&uuid=7ffedd04-878b-4649-89b2-61a5280cdcf1&query=Cat']
    rand_photo = random.choice(list)
    await message.answer_photo(photo= rand_photo, caption='Random photo')

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


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())