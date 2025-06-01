import random

def get_winner(choice1, choice2):
    if choice1 == choice2:
        return None  # ничья
    elif (choice1 == 'камень' and choice2 == 'ножницы') or \
            (choice1 == 'ножницы' and choice2 == 'бумага') or \
            (choice1 == 'бумага' and choice2 == 'камень'):
        return 1  # первый игрок победил
    else:
        return 2  # второй игрок победил

def valid_choice(choice):
    return choice in ['камень', 'ножницы', 'бумага']

def play_with_partner():
    scores = {1: 0, 2: 0}

    while scores[1] < 3 and scores[2] < 3:
        choice1 = input("Игрок 1, введите ваш выбор (камень, ножницы, бумага): ").lower()
        while not valid_choice(choice1):
            print("Некорректный ввод. Пожалуйста, введите 'камень', 'ножницы' или 'бумага'.")
            choice1 = input("Игрок 1, введите ваш выбор (камень, ножницы, бумага): ").lower()

        choice2 = input("Игрок 2, введите ваш выбор (камень, ножницы, бумага): ").lower()
        while not valid_choice(choice2):
            print("Некорректный ввод. Пожалуйста, введите 'камень', 'ножницы' или 'бумага'.")
            choice2 = input("Игрок 2, введите ваш выбор (камень, ножницы, бумага): ").lower()

        winner = get_winner(choice1, choice2)
        if winner:
            scores[winner] += 1
            print(f"Игрок {winner} победил в этом раунде!")
        else:
            print("Ничья!")

        print(f"Счет: Игрок 1 - {scores[1]}, Игрок 2 - {scores[2]}")

    overall_winner = 1 if scores[1] == 3 else 2
    print(f"Игрок {overall_winner} одержал победу в игре!")

def play_with_computer():
    choices = ['камень', 'ножницы', 'бумага']
    scores = {'Игрок': 0, 'Компьютер': 0}

    while scores['Игрок'] < 3 and scores['Компьютер'] < 3:
        player_choice = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()
        while not valid_choice(player_choice):
            print("Некорректный ввод. Пожалуйста, введите 'камень', 'ножницы' или 'бумага'.")
            player_choice = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()

        computer_choice = random.choice(choices)
        print(f"Компьютер выбрал: {computer_choice}")
        winner = get_winner(player_choice, computer_choice)
        if winner == 1:
            scores['Игрок'] += 1
            print("Вы победили в этом раунде!")
        elif winner == 2:
            scores['Компьютер'] += 1
            print("Компьютер победил в этом раунде!")
        else:
            print("Ничья!")

        print(f"Счет: Игрок - {scores['Игрок']}, Компьютер - {scores['Компьютер']}")

        overall_winner = 'Игрок' if scores['Игрок'] == 3 else 'Компьютер'
    print(f"{overall_winner} одержал победу в игре!")

def main():
        mode = input("Выберите режим игры: 1 - с партнером, 2 - с компьютером: ")
        if mode == '1':
            play_with_partner()
        elif mode == '2':
            play_with_computer()
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
        main()