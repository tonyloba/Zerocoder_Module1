"""
 Необходимо спарсить цены на диваны с сайта divan.ru в csv файл,
 обработать данные, найти среднюю цену и вывести ее,
 а также сделать гистограмму цен на диваны
"""

import time
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By

# Настройка Selenium
driver = webdriver.Chrome()

# Открытие страницы
url = 'https://www.divan.ru/category/divany-i-kresla'
driver.get(url)
time.sleep(5)

# Парсинг цен
prices = []
try:
    price_elements = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')
    for elem in price_elements:
        try:
            price_text = elem.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
            price = int(price_text.replace(' ', '').replace('руб.', '').strip())

        except Exception as e:
            print(f"Произошла ошибка при парсинге: {e}")
            continue

        prices.append(price)
finally:
    driver.quit()

# Запись данных в CSV
csv_filename = 'prices.csv'
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])
    for price in prices:
        writer.writerow([price])

# Обработка данных
prices_array = np.array(prices)
average_price = np.mean(prices_array)
print(f'Средняя цена: {average_price} ₽')

# Построение гистограммы
plt.hist(prices_array, bins=30, color='blue', edgecolor='black', alpha=0.7)
plt.title(f'Гистограмма цен на диваны со средней ценой: {average_price} ₽')
plt.xlabel('Цена (₽)')
plt.ylabel('Частота')
plt.show()