from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main_keyboard_test = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Тестовая кнопка 1")],
    [KeyboardButton(text="Тестовая кнопка 2"), KeyboardButton(text="Тестовая кнопка 3")]
], resize_keyboard=True)


inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Видео",url="https://www.youtube.com/" )],
])

test = ["кнопка 1", "кнопка 2", "кнопка 3", "кнопка 4"]

async def test_keyboard():
   keyboard = InlineKeyboardBuilder()
   for key in test:
       keyboard.add(KeyboardButton(text=key))
   return keyboard.adjust(2).as_markup()


# --- Задание 1: Простое меню ---
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
    ],
    resize_keyboard=True
)

# --- Задание 2: Кнопки с URL ---
links_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Новости", url="https://news.google.com/")],
        [InlineKeyboardButton(text="Музыка", url="https://music.youtube.com/")],
        [InlineKeyboardButton(text="Видео", url="https://www.youtube.com/")]
    ]
)

# --- Задание 3: Динамическая клавиатура ---
def dynamic_start_keyboard():
    """Кнопка 'Показать больше'"""
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Показать больше", callback_data="show_more")
    return keyboard.as_markup()

def dynamic_options_keyboard():
    """Опции после нажатия 'Показать больше'"""
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Опция 1", callback_data="option_1")
    keyboard.button(text="Опция 2", callback_data="option_2")
    return keyboard.as_markup()