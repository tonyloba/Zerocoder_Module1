import telebot
from telebot.types import Message
import requests

API_URL = 'http://127.0.0.1:8000/api'
BOT_TOKEN = ""
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message: Message):
    data = {'user_id': message.from_user.id, 'username': message.from_user.username}
    response = requests.post(f"{API_URL}/register_user/", json=data)
    if response.status_code == 200:
        if response.json().get('message'):
            bot.send_message(message.chat.id, "Вы уже были зарегистрированы ранее!")
        else:
            bot.send_message(message.chat.id,
                             f"Вы успешно зарегистрированы! Ваш уникальный номер: {response.json()['id']}")
    else:
        bot.send_message(message.chat.id, f"Произошла ошибка ри регистрации!")
        print(response.json())
        print(response.status_code)
        print(response.text)

# @bot.message_handler(commands=['myinfo'])
# def user_info(message: Message):
#     response = requests.get(f"{API_URL}/users/{message.from_user.id}/")
#
#     if response.status_code == 200:
#         user_data = response.json()
#         bot.reply_to(message, f"Ваша регистрация:\n\nID: {user_data['id']}\nUser ID: {user_data['user_id']}\nUsername: {user_data['username']}")
#     elif response.status_code == 404:
#         bot.send_message(message.chat.id, "Вы не зарегистрированы!")
#     else:
#         bot.send_message(message.chat.id, "Непредвиденная ошибка!")


@bot.message_handler(commands=['myinfo'])
def user_info(message: Message):
    response = requests.get(f"{API_URL}/users/{message.from_user.id}/")

    if response.status_code == 200:
        user_data = response.json()
        bot.reply_to(
            message,
            f"Ваша регистрация:\n\n"
            f"ID: {user_data['id']}\n"
            f"User ID: {user_data['user_id']}\n"
            f"Username: {user_data['username']}"
        )
    elif response.status_code == 404:
        bot.send_message(message.chat.id, "Вы не зарегистрированы!")
    else:
        bot.send_message(message.chat.id, "Непредвиденная ошибка!")

if __name__ == "__main__":
    bot.polling(none_stop=True)