import os
import telebot
import openai
from dotenv import load_dotenv
import os

load_dotenv()
# Инициализация API ключей
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://api.proxyapi.ru/openai/v1"

# Создание экземпляра бота
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Функция для обработки текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    '''

    '''


    try:
        # Запрос к OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": "user", "content": message.text}]
        )
        # Ответ модели
        ai_response = response['choices'][0]['message']['content']
        # Отправка ответа пользователю
        bot.reply_to(message, ai_response)
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка при обработке вашего запроса: {e}")

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен и готов принимать сообщения.")
    bot.infinity_polling()



# 1. **Импорт библиотек**: Мы импортируем необходимые библиотеки: `os` для работы с переменными окружения, `telebot` для работы с Telegram API, и `openai` для взаимодействия с OpenAI API.
#
# 2. **Инициализация API ключей**: Мы получаем токен Telegram-бота и ключ OpenAI API из переменных окружения. Это необходимо для аутентификации.
#
# 3. **Создание экземпляра бота**: Мы создаем экземпляр `TeleBot`, передавая ему токен нашего бота.
#
# 4. **Обработка сообщений**: Используем декоратор `@bot.message_handler` для обработки всех входящих текстовых сообщений. Функция `handle_message` отправляет пользовательское сообщение в OpenAI API и отправляет полученный ответ обратно пользователю.
#
# 5. **Запуск бота**: Метод `bot.infinity_polling()` запускает бота, позволяя ему бесконечно долго обрабатывать входящие сообщения.
#
# Этот код создает простого Telegram-бота, который отвечает на сообщения, используя модель GPT-3.5. Перед запуском убедитесь, что ваши переменные окружения (токен бота и ключ OpenAI) правильно настроены.