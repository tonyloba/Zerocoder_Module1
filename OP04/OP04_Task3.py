def bank(amount, years):
    for _ in range(years):
        amount += amount * 0.1
    return amount

initial_amount = float(input("Введите сумму вклада: "))
years = int(input("Введите количество лет: "))
final_amount = bank(initial_amount, years)
print(f"Сумма вклада через, {years} лет: {final_amount}")

