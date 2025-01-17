def concatenate_user_strings():
  # Запрашиваем первую строку у пользователя
  first_string = input("Введите первую строку:  ")

  # Запрашиваем вторую строку у пользователя
  second_string = input("Введите вторую строку: ")

  # Конкатенируем (объединяем) строки
  concatenated_string = first_string + second_string

  # Выводим результат на экран
  print("Результат конкатенации: ", concatenated_string)


# Вызов функции
concatenate_user_strings()
