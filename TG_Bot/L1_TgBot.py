import telebot

# Замените 'YOUR_API_KEY' на ваш фактический API-ключ Telegram-бота
API_KEY = '7947397986:AAESE_zpOAB8-cnj1l0jlefHgksNd81urys'
bot = telebot.TeleBot(API_KEY)


# Обработчик команды '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 "Добро пожаловать! Я ваш дружелюбный бот. Чем могу помочь?")


# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()

    if 'привет' in text:
        bot.reply_to(message, "Привет!")
    elif 'как дела' in text:
        bot.reply_to(message, "Я просто бот, но у меня всё хорошо!")
    elif 'вопрос' in text:
        bot.reply_to(message, "У вас есть вопрос? Я здесь, чтобы помочь!")
    else:
        bot.reply_to(message, "Я не уверен, как на это ответить.")


# Запуск бота
bot.polling()