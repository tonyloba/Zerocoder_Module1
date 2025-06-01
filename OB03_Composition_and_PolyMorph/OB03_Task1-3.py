class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass
    def move(self):
        pass
    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, type):
        super().__init__(name, age)
        self.type = type

    def make_sound(self):
        return "Chirp chirp"
    def move(self):
        return "Fly"
    def eat(self):
        return "Grass"

class Mammal(Animal):
    def __init__(self, name, age, type):
        super().__init__(name, age)
        self.type = type

    def make_sound(self):
        return "Roar"
    def move(self):
        return "Walk"
    def eat(self):
        return "Meat"

class Reptile(Animal):
    def __init__(self, name, age, type):
        super().__init__(name, age)
        self.type = type

    def make_sound(self):
        return "Hiss"
    def move(self):
        return "Crawl"
    def eat(self):
        return "Vegetables"

def animal_info(animal):
    try:
        print(f"The {animal.type} the {animal.name} makes a sound: {animal.make_sound()}")
        print(f"The {animal.type} the {animal.name} moves by: {animal.move()}")
        print(f"The {animal.type} the {animal.name} eats: {animal.eat()}")
        print("------------------------")
    except Exception as e:
        print(f"An error occurred: {e}")

list_animals = [Bird("Eagle", 5, "Bird"),
           Mammal("Lion", 10, "Mammal"),
           Reptile("Snake", 8, "Reptile")]

for animal in list_animals:
    animal_info(animal)