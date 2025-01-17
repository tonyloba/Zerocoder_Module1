def sum_range(start, end):
    sum: int = 0
    for i in range(start, end + 1):
        sum += i
    return sum

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
print(f"Сумма чисел в диапазоне "
      f"от {start} до {end}: {sum_range(start, end)}")
