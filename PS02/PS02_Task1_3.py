import pprint
import requests

#### Task 1:
response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
data = response.json()

print(data)
print(response.status_code)
pprint.pp(data['rates'])

#### Task 2:

url = "https://jsonplaceholder.typicode.com/posts"

params = {'userId': 1}

response = requests.get(url, params=params)

if response.status_code == 200:
    posts = response.json()
    for post in posts:
        print(f"Данные поста: {post}")
else:
    print(f"Ошибка при запросе данных: {response.status_code}")

#### Task 3:

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.post(url, json=data)

print(f"Статус-код: {response.status_code}")
print("Содержимое ответа:")
print(response.json())