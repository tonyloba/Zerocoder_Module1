import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.divan.ru/category/svet"
driver.get(url)
time.sleep(3)

# Названия классов берём с кода сайта
items = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

# Выводим вакансии на экран
print(items)
parsed_data = []

for item in items:
   try:
     title = item.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
     # price = item.find_element(By.CSS_SELECTOR, 'span.[data-testid="price"]').text
     price = item.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text


     #size = item.find_element(By.CSS_SELECTOR, 'span.vdukP pwHtE').text
   except:
     print("произошла ошибка при парсинге")
     continue

   parsed_data.append([title, price])

driver.quit()



# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("parsed_data_svet.csv", 'w',newline='', encoding='utf-8') as file:
    # Используем модуль csv и настраиваем запись данных в виде таблицы
    # Создаём объект
    writer = csv.writer(file)
    # Создаём первый ряд
    writer.writerow(['Название продукта', 'цена продукта'])

    # Прописываем использование списка как источника для рядов таблицы
    writer.writerows(parsed_data)