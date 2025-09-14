import sqlite3
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

from config import TOKEN

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# --- СОЗДАЁМ БАЗУ И ТАБЛИЦУ ---
def init_db():
    conn = sqlite3.connect("school_data.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

init_db()

# --- СОСТОЯНИЯ ---
class Form(StatesGroup):
    name = State()
    age = State()
    grade = State()

# --- Хэндлеры ---
@dp.message(Command('student_data'))
async def student_data(message: Message, state: FSMContext):
    await message.answer("Привет! Как тебя зовут?")
    await state.set_state(Form.name)

@dp.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Сколько тебе лет?")
    await state.set_state(Form.age)

@dp.message(Form.age)
async def process_age(message: Message, state: FSMContext):
    # Проверим, что возраст — число
    if not message.text.isdigit():
        await message.answer("Введите возраст числом, например: 15")
        return
    await state.update_data(age=int(message.text))
    await message.answer("В каком классе ты учишься? (например: 9А)")
    await state.set_state(Form.grade)

@dp.message(Form.grade)
async def process_grade(message: Message, state: FSMContext):
    await state.update_data(grade=message.text)
    user_data = await state.get_data()

    # --- Сохраняем в базу ---
    conn = sqlite3.connect("school_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO students (name, age, grade) VALUES (?, ?, ?)
        """, (user_data["name"], user_data["age"], user_data["grade"]))
    conn.commit()
    conn.close()

    await message.answer(
        f"✅ Данные сохранены!\n"
        f"Имя: {user_data['name']}\n"
        f"Возраст: {user_data['age']}\n"
        f"Класс: {user_data['grade']}"
    )

    await state.clear()


# --- Запуск бота ---
async def main():
    # Start the bot
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())