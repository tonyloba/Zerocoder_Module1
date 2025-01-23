def safe_divide(a=None, b=None):
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        return print(f"Результат деления: {a} / {b} = ",  a / b)
    except ZeroDivisionError:
        return None

safe_divide()