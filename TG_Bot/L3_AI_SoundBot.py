from tempfile import TemporaryDirectory
from dotenv import load_dotenv
import telebot
import openai
from gtts import gTTS
import os

load_dotenv()

# Создание экземпляра бота
SOUND_BOT_TOKEN = os.getenv("SOUND_BOT_TOKEN")
bot = telebot.TeleBot(SOUND_BOT_TOKEN)
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://api.proxyapi.ru/openai/v1"

# Функция для обработки текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    '''
    Обработка входящих сообщений и отправка голосового ответа.
    '''

    try:
        # Запрос к OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": "user", "content": message.text}]
        )
        # Ответ модели
        ai_response = response['choices'][0]['message']['content']

        # Создание голосового сообщения
        tts = gTTS(ai_response, lang='ru')
        audio_file = 'response.ogg'
        tts.save(audio_file)

        # Отправка голосового сообщения пользователю
        with open(audio_file, 'rb') as audio:
            bot.send_voice(message.chat.id, audio)

        # Удаление временного аудиофайла
        os.remove(audio_file)

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка при обработке вашего запроса: {e}")


# Запуск бота
if __name__ == "__main__":
    print("Бот запущен и готов принимать сообщения.")
    bot.infinity_polling()





# # Инициализация токена Telegram бота
# SOUND_BOT_TOKEN = os.getenv("SOUND_BOT_TOKEN")
#
# # Создание экземпляра бота
# bot = telebot.TeleBot(SOUND_BOT_TOKEN)
#
# # Функция для обработки текстовых сообщений
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     try:
#         # Создание временной директории для сохранения аудиофайла
#         with TemporaryDirectory() as tmpdirname:
#             # Преобразование текста в речь
#             tts = gTTS(text=message.text, lang='ru')
#             audio_path = os.path.join(tmpdirname, 'audio.mp3')
#             tts.save(audio_path)
#
#             # Отправка аудиофайла пользователю
#             with open(audio_path, 'rb') as audio:
#                 bot.send_voice(message.chat.id, audio)
#     except Exception as e:
#         bot.reply_to(message, f"Произошла ошибка при обработке вашего запроса: {e}")
#
# # Запуск бота
# if __name__ == "__main__":
#     print("Бот запущен и готов принимать сообщения.")
#     bot.infinity_polling()
#
# #
# # ### Объяснение:
# #
# # 1. **Импорт библиотек**: Мы используем `telebot` для взаимодействия с Telegram и `gTTS` для преобразования текста в речь.
# #
# # 2. **Инициализация токена**: Токен бота берется из переменных окружения. Убедитесь, что вы настроили переменные окружения или замените `os.getenv("TELEGRAM_BOT_TOKEN")` на строку с вашим токеном.
# #
# # 3. **Телеграм бот**: Мы создаем экземпляр `TeleBot` с вашим токеном.
# #
# # 4. **Обработка сообщений**: Декоратор `@bot.message_handler` используется для обработки всех текстовых сообщений. В функции `handle_message` мы преобразуем текст сообщения в аудио с помощью `gTTS` и
# # временно сохраняем его. Затем бот отправляет аудиофайл обратно пользователю.