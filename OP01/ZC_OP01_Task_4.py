def calculate_rectangle_area():
  # Запрашиваем длину прямоугольника у пользователя
  length = float(input("Введите длину прямоугольника: "))

  # Запрашиваем ширину прямоугольника у пользователя
  width = float(input("Введите ширину прямоугольника: "))

  # Вычисляем площадь прямоугольника
  area = length * width

  # Выводим результат на экран
  print("Площадь прямоугольника:", area)


# Вызов функции
calculate_rectangle_area()