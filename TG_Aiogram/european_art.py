import sqlite3
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
import requests
import random

from config import TOKEN, EUROPEANA_API_KEY  # <-- add your API key in config.py

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# --- Europeana API functions ---

def search_art_paintings(query="painting", rows=5):
    """
    Search for art paintings using Europeana API
    - Valid `TYPE` values include: `IMAGE`, `SOUND`, `TEXT`, `VIDEO`, `3D`, and more specific ones like `PAINTING`, `PHOTO`, `SCULPTURE`, etc
    """
    url = "https://api.europeana.eu/record/v2/search.json"
    params = {
        "wskey": EUROPEANA_API_KEY,
        "query": query,
        "qf": "TYPE:IMAGE",  # filter only images
        "rows": rows
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get("items", [])


def get_random_painting(query="painting"):
    """
    Get a random painting record from Europeana search results
    """
    items = search_art_paintings(query, rows=20)
    if not items:
        return None
    return random.choice(items)


# --- Bot Handlers ---

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Напиши мне тему или стиль картины, и я пришлю тебе изображение из Europeana.")


@dp.message()
async def send_painting(message: Message):
    query = message.text
    painting = get_random_painting(query)
    if painting:
        title = painting.get("title", ["Без названия"])[0]
        link = painting.get("guid", "Нет ссылки")
        edmPreview = painting.get("edmPreview", [None])[0]

        caption = f"🎨 {title}\n🔗 {link}"

        if edmPreview:
            await message.answer_photo(photo=edmPreview, caption=caption)
        else:
            await message.answer(caption)
    else:
        await message.answer("Картины по этому запросу не найдены. Попробуйте другой запрос.")

# --- Запуск бота ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())