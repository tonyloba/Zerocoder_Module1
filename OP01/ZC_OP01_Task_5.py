def get_exchange_rates():
    """
  Получить курсы валют. Можно использовать предустановленный курс или ввести вручную.
  """
    use_current_rates = input(
        "Вы хотите использовать текущий курс валют? (yes/no): ").strip().lower(
        )
    if use_current_rates == "yes":
        # Предустановленные курсы валют (пример)
        print("Используются текущие курсы валют:")
        print("1 USD = 101.68 RUB, 1 EUR = 106.10 RUB")
        return {'USD': 101.68, 'EUR': 106.10, 'RUB': 1.0}
    else:
        print("Введите актуальные курсы валют относительно рубля.")
        rates = {
            'USD': float(input("Введите курс доллара США к рублю: ")),
            'EUR': float(input("Введите курс евро к рублю: ")),
            'RUB': 1.0
        }
        return rates

def convert_currency(amount, from_currency, to_currency, rates):
    """
  Функция для конвертации суммы из одной валюты в другую.
  """
    # Конвертируем сумму в рубли
    amount_in_rub = amount * rates[from_currency]
    # Конвертируем из рублей в целевую валюту
    return amount_in_rub / rates[to_currency]

def main():
    # Получить курсы валют
    rates = get_exchange_rates()

    while True:
        # Ввод данных пользователя
        amount = float(input("Введите сумму для конвертации: "))
        print("Доступные валюты: RUB, USD, EUR")
        from_currency = input(
            "Введите код вашей исходной валюты: ").strip().upper()

        if from_currency not in rates:
            print("Ошибка: введен неверный код валюты.")
            continue

        print("Выберите целевую валюту: RUB, USD, EUR")
        to_currency = input("Введите код целевой валюты: ").strip().upper()

        if to_currency not in rates:
            print("Ошибка: введен неверный код валюты.")
            continue

        # Конвертация
        converted_amount = convert_currency(amount, from_currency, to_currency,
                                            rates)
        print(
            f"{amount:.2f} {from_currency} равно {converted_amount:.2f} {to_currency}"
        )

        # Спросить, нужен ли повтор
        repeat = input("Хотите выполнить еще одну конвертацию? (yes/no): "
                       ).strip().lower()
        if repeat != "yes":
            break

    print("Спасибо за использование конвертера валют!")


if __name__ == "__main__":
    main()
