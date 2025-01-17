def run_calc() -> None:

  def add(x, y):
    return x + y

  def subtract(x, y):
    return x - y

  def multiply(x, y):
    return x * y

  def divide(x, y):
    if y == 0:
      return "Ошибка: Деление на ноль!"
    return x / y

  # Бесконечный цикл, пока пользователь не решит выйти
  while True:
    print("Доступные операции:")
    print("1. Сложить")
    print("2. Вычесть")
    print("3. Умножить")
    print("4. Разделить")
    print("5. Выйти")

    # Ввод пользователя
    choice = input("Выберите операцию (1/2/3/4/5): ")

    # Проверяем, хочет ли пользователь выйти
    if choice == '5':
      print("Выход из программы...")
      break

    if choice in ('1', '2', '3', '4'):
      num1 = float(input("Введите первое число: "))
      num2 = float(input("Введите второе число: "))

      if choice == '1':
        print("Результат:", add(num1, num2))

      elif choice == '2':
        print("Результат:", subtract(num1, num2))

      elif choice == '3':
        print("Результат:", multiply(num1, num2))

      elif choice == '4':
        print("Результат:", divide(num1, num2))

    else:
      print("Неправильный ввод, попробуйте снова")

  if __name__ == "__main__":
    run_calc()
