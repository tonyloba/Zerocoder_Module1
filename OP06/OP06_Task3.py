import random

def select_random_students(students, num_to_choose=5):
    """
    - Принимает список имен `students` и количество имен для выбора `num_to_choose`.
    - Использует `random.sample` для выбора указанного количества уникальных имен.
    - Проверяет, что список содержит достаточно имен для выбора.
    """
    if len(students) < num_to_choose:
        raise ValueError("Количество учащихся меньше, чем количество требуемых для выбора.")

    # Случайный выбор уникальных имен из списка
    selected_students = random.sample(students, num_to_choose)
    return selected_students

students = [
    "Алексей", "Мария", "Иван", "Елена", "Дмитрий",
    "Ольга", "Сергей", "Анна", "Николай", "Татьяна",
    "Павел", "Юлия", "Андрей", "Екатерина", "Максим"
]

try:
    selected_students = select_random_students(students)
    print("Выбранные учащиеся для ответа на уроке:")
    for student in selected_students:
        print(student)
except ValueError as e:
    print(e)



