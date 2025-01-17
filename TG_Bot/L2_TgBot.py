import telebot

# Замените 'YOUR_API_TOKEN' на токен вашего бота
API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Я ваш Telegram бот. Используйте /help для вывода списка команд")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(
        message,
        "Вот список доступных команд:\n"
        "/start - Начать работу с ботом\n"
        "/help - Получить помощь\n"
        "/perevorot <текст> - Перевернуть текст\n"
        "/uppercase <текст> - Преобразовать текст в заглавные буквы\n"
        "/remove_vowels <текст> - Удалить гласные буквы из текста"
    )

# Обработчик команды /perevorot
@bot.message_handler(commands=['perevorot'])
def reverse_text(message):
    # Получение текста после команды
    parts = message.text.split(maxsplit=1)
    if len(parts) == 2:
        text_to_reverse = parts[1]
        # Переворачиваем текст
        reversed_text = text_to_reverse[::-1]
        bot.reply_to(message, reversed_text)
    else:
        bot.reply_to(message, "Пожалуйста, укажите текст для переворота после команды /perevorot.")

# Обработчик команды /uppercase
@bot.message_handler(commands=['uppercase'])
def uppercase_text(message):
    # Получение текста после команды
    parts = message.text.split(maxsplit=1)
    if len(parts) == 2:
        text_to_uppercase = parts[1]
        # Преобразуем текст в заглавные буквы
        uppercase_text = text_to_uppercase.upper()
        bot.reply_to(message, uppercase_text)
    else:
        bot.reply_to(message, "Пожалуйста, укажите текст для преобразования в заглавные буквы после команды /uppercase.")

# Обработчик команды /remove_vowels
@bot.message_handler(commands=['remove_vowels'])
def remove_vowels_text(message):
    # Получение текста после команды
    parts = message.text.split(maxsplit=1)
    if len(parts) == 2:
        text_to_modify = parts[1]
        # Удаляем гласные буквы
        vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
        modified_text = ''.join([char for char in text_to_modify if char not in vowels])
        bot.reply_to(message, modified_text)
    else:
        bot.reply_to(message, "Пожалуйста, укажите текст для удаления гласных букв после команды /remove_vowels.")

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен и ожидает сообщений...")
    bot.polling(none_stop=True)