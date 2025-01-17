def compress_string(s: str) -> str:
    if not s:  # Проверка на пустую строку
        return ""

    compressed = []  # Список для хранения сжатой строки
    count = 1  # Счётчик повторов символов

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  # Если текущий символ равен предыдущему
            count += 1
        else:
            # Добавляем символ и его количество в список
            compressed.append(s[i - 1] + str(count))
            count = 1  # Сбрасываем счётчик

    # Добавляем последний символ и его количество
    compressed.append(s[-1] + str(count))

    return ''.join(compressed)  # Объединяем список в строку


#input_string = "aabrrrrryyyyycccccaaa"
input_string = input("Ввведите произвольный набор букв без пробелов: ")
result = compress_string(input_string)
print("Сжатая строка:", result)
