from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')  # Загружает переменные из .env
API_KEY = os.getenv('API_NINJAS_KEY')

app = Flask(__name__)

@app.route('/')
def index():
    api_url = 'https://api.api-ninjas.com/v1/quotes'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        data = response.json()
        quote = data[0]['quote']
        author = data[0]['author']
    else:
        print("Error:", response.status_code, response.text)
        quote = "Не удалось получить цитату."
        author = ""
    return render_template('index.html', quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True)
