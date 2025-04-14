import telebot
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("Linux_Kali_BOT_KEY")
bot = telebot.TeleBot(TOKEN)

# Обработчик для приёма текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "этот бот лежит на локальном сервере")

# Запуск бота
bot.polling()

#########################
import telebot

# Замените 'YOUR_BOT_TOKEN' на токен, который вы получили от BotFather
TOKEN = '7776997024:AAGGTwcnNU2klvDG5LeIvrjJiD1IUJ1DT7E'
bot = telebot.TeleBot(TOKEN)

# Обработчик для приёма текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "этот бот лежит на локальном сервере")

# Запуск бота
bot.polling()