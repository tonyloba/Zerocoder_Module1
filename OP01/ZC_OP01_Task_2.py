def main():
  # Запрашиваем имя и возраст
  name = input("Введите ваше имя: ").strip()
  age = int(input("Введите ваш возраст (полных лет): "))

  # Приветствие
  print(f"\nПривет, {name}! Тебе {age} лет.")

  # Расчеты
  years = age
  months = years * 12
  days = years * 365  # Упрощенно, без учета високосных лет
  hours = days * 24
  seconds = hours * 3600

  # Вывод результатов
  print(
      "\nСколько времени ты прожил(а) в рамках отдельного временного диапазона:"
  )
  print(f"- Лет: {years}")
  print(f"- Месяцев: {months}")
  print(f"- Дней: {days}")
  print(f"- Часов: {hours}")
  print(f"- Секунд: {seconds}")


# Запуск программы
if __name__ == "__main__":
  main()
