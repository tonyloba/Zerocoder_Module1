
def int_request():

    try:
        user_input = input("Введите значение: ")
        number = int(user_input)
        # number = int(user_input)
        print(f"Целочисленное значение: {number}")
    except ValueError:
        print("Ошибка: введено не целое число.")
    except TypeError:
        print("Ошибка: неправильный тип данных.")
    except KeyboardInterrupt:
        print("Ошибка: ввод был прерван пользователем.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

int_request()