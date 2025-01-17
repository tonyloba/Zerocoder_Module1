def collect_user_input():
    user_inputs = []  # Инициализируем пустой список для хранения ввода

    # Цикл будет выполняться 10 раз
    for i in range(10):
        user_input = input(f"Введите символ или цифру ({i + 1}): ")
        user_inputs.append(user_input)  # Добавляем введенный символ в список

    print("Вы ввели следующие символы/цифры:", user_inputs)

# Вызов функции
collect_user_input()