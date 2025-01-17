def three_numbers():
    # Запрашиваем у пользователя три числа
    number1 = float(input("Введите первое число: "))
    number2 = float(input("Введите второе число: "))
    number3 = float(input("Введите третье число: "))

    # Находим наименьшее число с помощью функции min
    smallest = min(number1, number2, number3)

    # Выводим наименьшее число
    print(f"Наименьшее число: {smallest}")
def three_numbers_opt2():
    # Запрашиваем у пользователя три числа
    number1 = float(input("Введите первое число: "))
    number2 = float(input("Введите второе число: "))
    number3 = float(input("Введите третье число: "))
    # Используем if, elif и else для определения наименьшего числа
    if number1 < number2 and number1 < number3:
        smallest = number1
    elif number2 < number1 and number2 < number3:
        smallest = number2
    else:
        smallest = number3
    # Выводим наименьшее число
    print(f"Наименьшее число: {smallest}")

three_numbers()
three_numbers_opt2()