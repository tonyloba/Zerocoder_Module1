class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        return "Some sound"
    def eat(self, food):
        print(f"{self.name} is eating {food}.")
class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

    def fly(self):
        print(f"{self.name} is flying.")
class Mammal(Animal):
    def make_sound(self):
        return "Roar!"

class Reptile(Animal):
    def make_sound(self):
        return "Hiss!"

def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} says: {animal.make_sound()}")

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []
    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"Added {animal.name} to the zoo.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Added staff member: {staff_member.name}.")

    def show_animals(self):
        for animal in self.animals:
            print(f"Animal: {animal.name}, Age: {animal.age}")

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal, food):
        print(f"{self.name} is feeding {animal.name}.")
        animal.eat(food)

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")

# Пример использования классов
if __name__ == "__main__":
    # Создаем животных
    parrot = Bird("Polly", 2)
    lion = Mammal("Simba", 5)
    snake = Reptile("Slytherin", 3)

    # Демонстрируем полиморфизм
    animal_sound([parrot, lion, snake])

    # Создаем зоопарк
    my_zoo = Zoo()
    my_zoo.add_animal(parrot)
    my_zoo.add_animal(lion)
    my_zoo.add_animal(snake)

    # Создаем сотрудников
    keeper = ZooKeeper("John")
    vet = Veterinarian("Dr. Smith")

    my_zoo.add_staff(keeper)
    my_zoo.add_staff(vet)

    # Показываем всех животных в зоопарке
    my_zoo.show_animals()

    # Зоосмотритель кормит животных
    keeper.feed_animal(parrot, "seeds")
    keeper.feed_animal(lion, "meat")

    # Ветеринар лечит животное
    vet.heal_animal(snake)
