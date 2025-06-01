import random
'''

1. **Класс `Hero`:**
   - Конструктор `__init__` инициализирует имя героя, здоровье и силу удара.
   - Метод `attack` уменьшает здоровье другого героя на величину силы удара.
   - Метод `is_alive` проверяет, жив ли герой (здоровье больше 0).

2. **Класс `Game`:**
   - Конструктор `__init__` создает двух героев: игрока и компьютер.
   - Метод `start` запускает игру и чередует ходы между игроком и компьютером, пока один из них не проиграет.
   - Метод `display_health` выводит текущее здоровье обоих героев.

'''
class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        self.player = Hero(name="Игрок")
        self.computer = Hero(name="Компьютер")

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            self.display_health()

            if not self.computer.is_alive():
                print("Игрок победил!")
                break

            self.computer.attack(self.player)
            self.display_health()

            if not self.player.is_alive():
                print("Компьютер победил!")
                break

    def display_health(self):
        print(f"Здоровье {self.player.name}: {self.player.health}")
        print(f"Здоровье {self.computer.name}: {self.computer.health}")
        print("="*30)

if __name__ == "__main__":
    game = Game()
    game.start()