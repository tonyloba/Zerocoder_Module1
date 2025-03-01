from abc import ABC, abstractmethod

# Шаг 1: Создайте абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуйте конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

class Bow(Weapon):
    def attack(self):
        return "стреляет из лука"

# Шаг 3: Модифицируйте класс Fighter
# Класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {type(weapon).__name__}.")

    def attack(self, monster):
        if self.weapon is None:
            print(f"{self.name} не имеет оружия для атаки!")
        else:
            action = self.weapon.attack()
            print(f"{self.name} {action}.")
            monster.defeat()

# Класс Monster
class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        print(f"{self.name} побежден!")

# Шаг 4: Реализация боя
def main():
    fighter = Fighter("Боец")
    monster = Monster("Монстр")

    sword = Sword()
    bow = Bow()

    # Боец выбирает меч
    fighter.change_weapon(sword)
    fighter.attack(monster)

    # Боец выбирает лук
    fighter.change_weapon(bow)
    fighter.attack(monster)

if __name__ == "__main__":
    main()