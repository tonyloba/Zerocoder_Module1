def sum_range(start, end):
    """
    Добавление к задаче OP04_Task1.py ошибок с Try-Except
    """
    total: int = 0
    for i in range(start, end + 1):
        total += i
    return total

try:
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))
    print(f"Сумма чисел в диапазоне от {start} до {end}: {sum_range(start, end)}")

except ValueError as ve:
    print("Ошибка: введите целое число. Подробности ошибки: ", ve)

except KeyboardInterrupt:
    print("\nОшибка: ввод был прерван пользователем.")

except Exception as e:
    print("Произошла ошибка: ", e)