def union_of_sets():
    def get_set_from_user(prompt):
        while True:
            try:
                user_input = input(prompt)
                # Преобразуем введенную строку в множество
                user_set = set(map(int, user_input.split()))
                return user_set
            except ValueError:
                print("Пожалуйста, введите числа, разделенные пробелами.")

    print("Введите элементы первого множества, разделенные пробелами:")
    set1 = get_set_from_user("Первое множество: ")

    print("Введите элементы второго множества, разделенные пробелами:")
    set2 = get_set_from_user("Второе множество: ")

    # Объединяем множества
    # union_set = set1 | set2
    union_set = set1.union(set2)
    # Выводим результат
    print("Результат объединения множеств:", union_set)

# Вызов функции
union_of_sets()