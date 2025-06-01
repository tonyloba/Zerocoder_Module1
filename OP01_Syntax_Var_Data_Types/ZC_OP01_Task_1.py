def perform_operations():
  # Ввод чисел пользователем
  num1 = float(input("Введите первое число: "))
  num2 = float(input("Введите второе число: "))

  # Выполнение операций
  addition = num1 + num2
  subtraction = num1 - num2
  multiplication = num1 * num2
  division = num1 / num2 if num2 != 0 else "Деление на ноль невозможно"
  floor_division = num1 // num2 if num2 != 0 else "Целая часть от деления на ноль невозможна"
  remainder = num1 % num2 if num2 != 0 else "Остаток от деления на ноль невозможен"
  power = num1 ** num2

  # Вывод результатов
  print("\nРезультаты операций:")
  print(f"Сложение: {num1} + {num2} = {addition}")
  print(f"Вычитание: {num1} - {num2} = {subtraction}")
  print(f"Умножение: {num1} * {num2} = {multiplication}")
  print(f"Деление: {num1} / {num2} = {division}")
  print(f"Целая часть от деления: {num1} // {num2} = {floor_division}")
  print(f"Остаток от деления: {num1} % {num2} = {remainder}")
  print(f"Возведение в степень: {num1} ** {num2} = {power}")

# Запуск программы
perform_operations()