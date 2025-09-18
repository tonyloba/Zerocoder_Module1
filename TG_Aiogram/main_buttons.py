import asyncio
from aiogram import Bot, Dispatcher,F, types
from aiogram.filters.command import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, FSInputFile,KeyboardButton,CallbackQuery
import os
import logging
import keyboard as kb

logging.basicConfig(level=logging.INFO)

from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher()

# @dp.message(CommandStart())
# async def start(message: Message):
#     await message.answer(f'Hi {message.from_user.first_name}! I am a bot!',reply_markup=kb.main_keyboard)
#     # Inline Buttons :
#     # await message.answer(f'Hi {message.from_user.first_name}! I am a bot!',reply_markup=kb.inline_keyboard)
#     # Keyboard Builder
#     # await message.answer(f'Hi {message.from_user.first_name}! I am a bot!',reply_markup=kb.test_keyboard())


# --- Задание 1 ---
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! Я бот!",
        reply_markup=kb.main_keyboard
    )

# Реакция на кнопки "Привет" и "Пока"
@dp.message(F.text == "Привет")
async def hello_button(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(F.text == "Пока")
async def bye_button(message: Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")


# --- Задание 2 ---
@dp.message(Command("links"))
async def links(message: Message):
    await message.answer("Вот полезные ссылки:", reply_markup=kb.links_keyboard)


#--- Задание 3 ---
@dp.message(Command("dynamic"))
async def dynamic(message: Message):
    await message.answer("Нажми кнопку:", reply_markup=kb.dynamic_start_keyboard())

@dp.callback_query(F.data == "show_more")
async def show_more(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выберите опцию:",
        reply_markup=kb.dynamic_options_keyboard()
    )

@dp.callback_query(F.data == "option_1")
async def option_1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Вы выбрали: Опция 1")

@dp.callback_query(F.data == "option_2")
async def option_2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Вы выбрали: Опция 2")



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())