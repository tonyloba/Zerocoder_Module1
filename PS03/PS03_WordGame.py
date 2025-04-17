import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# ИГРА УГАДАЙ СЛОВО (Создаём функцию, которая будет получать информацию)
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word_eng = word_dict.get("english_words")
        word_definition_eng = word_dict.get("word_definition")

        # Переводим слово с английского на русский
        translator = Translator()
        translation = translator.translate(word_eng, src="en", dest="ru")
        word = translation.text

        # Переводим описание слова с английского на русский
        translation = translator.translate(word_definition_eng, src="en", dest="ru")
        word_definition = translation.text


        # Начинаем игру
        print(f"Значение слова на английском - {word_definition_eng}")
        print(f"Значение слова на русском - {word_definition}")

        user = input("Что это за слово? ")
        for _ in range(2):
            if user != word and user != word_eng:
                print("Неправильно, попробуйте ещё раз")
                user = input("Что это за слово? ")
        if user == word or user == word_eng:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово на русском - {word} и на английском - {word_eng}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n : ")
        if play_again != "y":
            print("Спасибо за игру!")
            break


word_game()