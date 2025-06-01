def text_to_file():
    # Запрашиваем текст у пользователя
    user_input = input("Введите текст, который хотите записать в файл: ")

    # Открываем файл в режиме записи (если файла нет, онs будет создан)
    with open("OP06_Files_and_Modules/user_data.txt", "w", encoding="utf-8") as file:
        # Записываем введенный текст в файл
        file.write(user_input)

    print("Текст успешно записан в файл user_data.txt.")

text_to_file()