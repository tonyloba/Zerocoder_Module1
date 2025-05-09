from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

def search_wikipedia(query):
    browser = webdriver.Firefox()
    browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
    assert "Википедия" in browser.title

    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(query)
    time.sleep(1)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    return browser

def display_paragraphs(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for i, paragraph in enumerate(paragraphs[:5], 1):
        print(f"{i}. {paragraph.text}\n")

def get_related_links(browser):
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable ts-main":
            hatnotes.append(element)
    if hatnotes:
        hatnote = random.choice(hatnotes)
        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    else:
        print("Нет связанных страниц.")
        return None
    return link


def main():
    find_word = input("Что ищем? ")
    browser = search_wikipedia(find_word)

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        choice = input("Введите номер действия: ")

        if choice == "1":
            display_paragraphs(browser)
        elif choice == "2":
            link = get_related_links(browser)
            if link:
                browser.get(link)
        elif choice == "3":
            browser.quit()
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()