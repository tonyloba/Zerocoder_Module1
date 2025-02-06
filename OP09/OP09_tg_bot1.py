import smtplib
from email.mime.text import MIMEText
import telebot
from telebot import types
import schedule
import time
import threading
from smtplib import SMTP
from dotenv import load_dotenv
import os

def start_bot():
    """
    Этот код создает бота, который взаимодействует с пользователем,
    запрашивает информацию о предпочтениях в диете и затем
    отправляет соответствующие предложения питания в указанные временные интервалы в чат
    и полное меню на указанную почту.
    """

    load_dotenv()
    print("Бот запущен")
    LA_DIET_TOKEN = os.getenv("LA_DIET_TOKEN")

    # Создание экземпляра бота
    bot = telebot.TeleBot(LA_DIET_TOKEN)

    user_data = {}

    diet_options = {
        "Вегетарианская": ["овощное рагу", "тофу с овощами", "тыквенный суп", "салат из капусты"],
        "Средиземноморская диета": ["греческий салат", "рыба на гриле", "хумус с овощами", "паста с томатами"],
        "Кето-диета": ["бекон с авокадо", "омлет с сыром", "салат из тунца", "курица на гриле"],
        "Палео-диета": ["стейк с овощами", "яйца с беконом", "курица с зеленью", "овощное рагу"],
        "Без Диеты": ["бутерброд", "суп", "паста", "пицца"]
    }

    def send_email(email, message, meals):
        try:
            # Настройте SMTP сервер для отправки почты
            with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as smtp:
                smtp.starttls()
                smtp.login("3e10ead63178e7", "59556104f352eb")
                meal_info = "\n".join(
                    [f"{meal}: {dish}" for meal, dish in zip(["Завтрак", "Обед", "Полдник", "Ужин"], meals)])
                msg = MIMEText(f"{message}\n\nВаши приемы пищи на день:\n{meal_info}", 'plain', 'utf-8')
                msg['Subject'] = 'Ваше питание на день'
                msg['From'] = "superdiet@yahoo.com"
                msg['To'] = email
                smtp.sendmail("superdiet@yahoo.com", email, msg.as_string())
                print(f"Письмо успешно отправлено на {email}")
        except Exception as e:
            print(f"Ошибка при отправке письма: {e}")

    def schedule_meals(chat_id):
        # Получаем список приемов пищи
        user_diet = user_data[chat_id]['diet']
        meals = diet_options[user_diet]

        def send_breakfast():
            bot.send_message(chat_id, f"Ваш завтрак: {meals[0]}")

        def send_lunch():
            bot.send_message(chat_id, f"Ваш ланч: {meals[1]}")

        def send_snack():
            bot.send_message(chat_id, f"Ваш полдник: {meals[2]}")

        def send_dinner():
            bot.send_message(chat_id, f"Ваш ужин: {meals[3]}")

        # Запланированная отправка сообщений
        schedule.every().day.at("06:00").do(send_breakfast)
        schedule.every().day.at("12:00").do(send_lunch)
        schedule.every().day.at("15:00").do(send_snack)
        schedule.every().day.at("00:14").do(send_dinner)

        # Отправка письма с информацией о всех приемах пищи
        send_email(user_data[chat_id]['email'], "Добро пожаловать! Мы рады, что вы выбрали наш бот для планирования питания.", meals)

    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    # Стартовый пункт
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        chat_id = message.chat.id
        user_data[chat_id] = {}
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add("Вегетарианская", "Средиземноморская диета", "Кето-диета", "Палео-диета", "Без Диеты")
        msg = bot.reply_to(message, "Какую диету вы предпочитаете?", reply_markup=markup)
        bot.register_next_step_handler(msg, process_diet_step)

    def process_diet_step(message):
        chat_id = message.chat.id
        diet = message.text
        user_data[chat_id]['diet'] = diet
        msg = bot.reply_to(message, "Перечислите типы продуктов, которые вы хотите использовать (например, курица, овощи)")
        bot.register_next_step_handler(msg, process_food_types_step)

    def process_food_types_step(message):
        chat_id = message.chat.id
        user_data[chat_id]['food'] = message.text
        msg = bot.reply_to(message, "Укажите электронную почту, куда отправить результат:")
        bot.register_next_step_handler(msg, process_email_step)

    def process_email_step(message):
        chat_id = message.chat.id
        email = message.text
        user_data[chat_id]['email'] = email

        user_diet = user_data[chat_id]['diet']
        meals = diet_options.get(user_diet, [])

        bot.send_message(chat_id, "Спасибо! Варианты питания будут отправлены по указанным временным интервалам.")
        schedule_meals(chat_id)

        send_email(email, "Добро пожаловать! Мы рады, что вы выбрали наш бот для планирования питания.", meals)

    # Запустить поток для планировщика
    threading.Thread(target=run_schedule).start()

    # Запустить бота
    bot.polling(none_stop=True)

# Вызов функции для запуска бота
start_bot()
