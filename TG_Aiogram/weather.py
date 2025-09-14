import sqlite3
import asyncio
import os
import aiohttp
import logging
from aiogram import Bot, Dispatcher,F, types
from aiogram.filters.command import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, FSInputFile,KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

from config import TOKEN, WEATHER_API_KEY

# Initialize bot with storage
storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)

logging.basicConfig(level=logging.INFO)



class Form(StatesGroup):
    name = State()
    age = State()
    city = State()

def init_db():
    conn = sqlite3.connect('users_data.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users 
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    city TEXT NOT NULL)''')

    conn.commit()
    conn.close()

init_db()


@dp.message(Command('get_weather'))
async def get_weather(message: Message, state: FSMContext):
    await message.answer('Hi what is your name?')
    await state.set_state(Form.name)


@dp.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('How old are you?')
    await state.set_state(Form.age)

@dp.message(Form.age)
async def process_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Where are you from(City)?')
    await state.set_state(Form.city)

@dp.message(Form.city)
async def process_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    user_data = await state.get_data()

    conn = sqlite3.connect('users_data.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (name, age, city) VALUES (?, ?, ?)
    ''', (user_data['name'], user_data['age'], user_data['city'])
    )
    conn.commit()
    conn.close()
    await message.answer('Thank you for your data!')
    await state.clear()

    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_data['city']}&appid={WEATHER_API_KEY}&units=metric&lang=ru") as response:
            if response.status == 200:
                weather_data = await response.json()
                main = weather_data['main']
                weather = weather_data['weather'][0]
                temperature = main['temp']
                humidity = main['humidity']
                description = weather['description']

                weather_info = (f" City - {user_data['city']} \n"
                                f" Temperature: {temperature}°C\n"
                                f" Humidity: {humidity}%\n"
                                f" Description: {description.capitalize()}")

                await message.answer(weather_info)
            else:
                await message.answer('No data found')

        await state.clear()


async def main():
    # Start the bot
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())