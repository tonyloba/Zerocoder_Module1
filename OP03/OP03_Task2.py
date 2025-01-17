def simple_calc():
    while True:
        user_input = input("Хотите использовать калькулятор? (да/нет): ")
        if user_input.lower() == 'нет':
            print("Выход из программы.")
            break
        else:
            print("Активируем калькулятор:")
        try:
            number1 = float(input("Введите первое число: "))
            number2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введите числовые значения.")
            continue
        operation = input("Введите операцию (+, -, *, /): ")
        while operation not in ['+', '-', '*', '/']:
            print("Недопустимая операция. Пожалуйста, выберите одну из: +, -, *, /.")
            operation = input("Введите операцию (+, -, *, /): ")
        # Выполняем операцию на основании выбора пользователя
        if operation == "+":
            result = number1 + number2
            print(f"Результат: {number1} + {number2} = {result}")
        elif operation == "-":
            result = number1 - number2
            print(f"Результат: {number1} - {number2} = {result}")
        elif operation == "*":
            result = number1 * number2
            print(f"Результат: {number1} * {number2} = {result}")
        elif operation == "/":
            if number2 != 0:  # Проверяем, чтобы делитель не был равен нулю
                result = number1 / number2
                print(f"Результат: {number1} / {number2} = {result}")
            else:
                print("Ошибка: деление на ноль!")
simple_calc()