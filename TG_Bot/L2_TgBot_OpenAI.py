import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_ai():
    print("Введите 'exit', чтобы выйти из чата.")
    while True:
        user_input = input("Вы: ")
        if user_input.lower() == "exit":
            print("Чат завершен.")
            break

        # Запрос к OpenAI API
        try:
            response = openai.Completion.create(
                model="gpt-3.5-turbo",
                prompt=user_input,
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7
            )

            # Получение и вывод ответа
            ai_response = response.choices[0].text.strip()
            print(f"Ассистент: {ai_response}")

        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    chat_with_ai()

# client = OpenAI()
#
# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "Write a haiku about recursion in programming."
#         }
#     ]
# )