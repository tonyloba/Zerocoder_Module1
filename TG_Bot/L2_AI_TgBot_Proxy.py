import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://api.proxyapi.ru/openai/v1"
def chat_with_ai():
    """
    1. **Инициализация клиента**: Используется API ключ и базовый URL, чтобы создать клиента OpenAI.
    2. **Цикл общения**: Программа ожидает ввод от пользователя. Если пользователь вводит "exit", программа завершает работу.
    3. **Отправка запроса**: Пользовательский ввод отправляется на сервер OpenAI, и API возвращает ответ.
    4. **Вывод ответа**: Ответ от нейросети выводится в консоль.
    """
    print("Введите 'exit', чтобы выйти из чата.")
    while True:
        user_input = input("Вы: ")
        if user_input.lower() == "exit":
            print("Чат завершен.")
            break
        try:
            # Запрос к OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            # Ответ модели
            ai_response = response['choices'][0]['message']['content']
            print(f"Ассистент: {ai_response}")

        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    chat_with_ai()


