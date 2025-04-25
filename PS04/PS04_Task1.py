from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def get_paragraphs(driver):
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    for i, paragraph in enumerate(paragraphs):
        print(f"\nПараграф {i + 1}:\n")
        print(paragraph.text)
        if input("\nНажмите Enter для продолжения или введите 'q' для выхода из параграфов: ") == 'q':
            break

def choose_link(driver):
    links = driver.find_elements(By.CSS_SELECTOR, "#bodyContent a")
    link_texts = [link.text for link in links if link.text]

    if not link_texts:
        print("Нет связанных страниц.")
        return None

    for i, link_text in enumerate(link_texts, start=1):
        print(f"{i}. {link_text}")

    choice = input("Введите номер статьи, чтобы перейти на неё, или 'b' для возврата: ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(link_texts):
            return links[choice - 1].get_attribute('href')

    return None

def main():
    driver = webdriver.Chrome()  # Убедитесь, что путь к ChromeDriver указан верно
    try:
        query = input("Введите запрос для поиска на Википедии: ")
        driver.get("https://ru.wikipedia.org/wiki/" + query.replace(' ', '_'))

        while True:
            print(f"\n--- {driver.title} ---\n")
            action = input("Выберите действие:\n1. Листать параграфы статьи\n2. Перейти на связанную страницу\n3. Выйти из программы\nВаш выбор: ")

            if action == '1':
                get_paragraphs(driver)
            elif action == '2':
                new_url = choose_link(driver)
                if new_url:
                    driver.get(new_url)
            elif action == '3':
                print("Выход из программы.")
                break
            else:
                print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()