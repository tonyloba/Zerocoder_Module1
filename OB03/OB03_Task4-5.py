import json
import time

class ZooKeeper:
    def __init__(self, name):
        self.name = name
        self.position = "ZooKeeper"

    def __str__(self):
        return f"{self.name} ({self.position})"

    def feed_animal(self, animal):
        print(f"{self.name} кормит животное {animal['name']}.")

class Veterinarian:
    def __init__(self, name):
        self.name = name
        self.position = "Veterinarian"

    def __str__(self):
        return f"{self.name} ({self.position})"

    def heal_animal(self, animal):
        print(f"{self.name} лечит животное {animal['name']}.")

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, name, species, age):
        animal = {
            "name": name,
            "species": species,
            "age": age
        }
        self.animals.append(animal)
        print(f"Добавлено животное: {animal['name']} ({animal['species']})")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Добавлен сотрудник: {employee}")

    def list_animals(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f" - {animal['name']} ({animal['species']})")

    def list_employees(self):
        print("Сотрудники зоопарка:")
        for employee in self.employees:
            print(f" - {employee}")

    def save_to_file(self, filename):
        data = {
            "animals": self.animals,
            "employees": [{"name": employee.name, "position": employee.position} for employee in self.employees]
        }
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
        print(f"Data saved to {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
            self.animals = data["animals"]
            self.employees = [ZooKeeper(employee["name"]) if employee["position"] == "ZooKeeper" else Veterinarian(employee["name"]) for employee in data["employees"]]
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty zoo.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filename}. Starting with an empty zoo.")

# Взаимодействие сотрудников с животными и проверка наличия сотрудников и животных
    def feed_animal(self, employee_name, animal_name):
        for employee in self.employees:
            if employee.name == employee_name and isinstance(employee, ZooKeeper):
                for animal in self.animals:
                    if animal["name"] == animal_name:
                        employee.feed_animal(animal)
                        return
                print(f"Животное {animal_name} не найдено.")
                return
        print(f"Сотрудник {employee_name} не найден или не является зоооператором.")

    def heal_animal(self, employee_name, animal_name):
        for employee in self.employees:
            if employee.name == employee_name and isinstance(employee, Veterinarian):
                for animal in self.animals:
                    if animal["name"] == animal_name:
                        employee.heal_animal(animal)
                        return
                print(f"Животное {animal_name} не найдено.")
                return
        print(f"Сотрудник {employee_name} не найден или не является ветеринаром.")


zoo = Zoo("Городской Зоопарк")

# Загрузка данных из файла
zoo.load_from_file('zoo_data.json')
time.sleep(3)

# Добавляем животных
zoo.add_animal("Лев", "Пантеры", 5)
zoo.add_animal("Слон", "Африканский слон", 10)

# Добавляем сотрудников
zoo.add_employee(ZooKeeper("Анна"))
zoo.add_employee(Veterinarian("Иван"))

# Вариант вывода списка 1:
zoo.list_animals()
zoo.list_employees()

# Вариант вывода списка 2 :
print("Animals:")
for animal in zoo.animals:
    print(f" - {animal['name']} ({animal['species']})")

print("Employees:")
for employee in zoo.employees:
    print(f" - {employee}")

# Взаимодействие сотрудников с животными
zoo.feed_animal("Анна", "Лев")
zoo.heal_animal("Иван", "Слон")

# Сохранение данных в файл
zoo.save_to_file('zoo_data.json')



##################################
#   Alternative code with decorators

# import json
#
# class Animal:
#
#   """
    # I used the @classmethod decorator in the Animal and Employee classes to define the from_dict method as a class method.
    # Here, class method is a method that is bound to the class itself, rather than to an instance of the class.
    # This means that a class method can be called on the class directly, without creating an instance of the class.
    # I used @classmethod for the from_dict method because it is a method that creates a new instance of the class from a dictionary.
    # This method does not depend on any specific instance of the class, but rather on the class itself. By defining it as a class method,
    # I can call it on the class directly, like this: Animal.from_dict(data).
    # Using @classmethod also allows me to use the class name Animal or Employee inside the method,
    # which is useful for creating new instances of the class.
    # In this example, cls is a reference to the class itself, which is Animal or Employee.
    # The method creates a new instance of the class by calling the class constructor (cls(data["name"], data["species"]))
    # and returns the new instance.
    #
    # By using @classmethod, I can define a method that is closely tied to the class itself,
    # and that can be used to create new instances of the class from a dictionary.

#   """

#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#     def __str__(self):
#         return f"{self.name} ({self.species})"
#
#     def to_dict(self):
#         return {
#             "name": self.name,
#             "species": self.species
#         }
#
#     @classmethod
#     def from_dict(cls, data):
#         return cls(data["name"], data["species"])
#
# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
#     def __str__(self):
#         return f"{self.name} ({self.position})"
#
#     def to_dict(self):
#         return {
#             "name": self.name,
#             "position": self.position
#         }
#
#     @classmethod
#     def from_dict(cls, data):
#         return cls(data["name"], data["position"])
#
# class ZooKeeper(Employee):
#     def __init__(self, name):
#         super().__init__(name, "ZooKeeper")
#
#     def feed_animal(self, animal):
#         print(f"{self.name} кормит животное {animal.name}.")
#
# class Veterinarian(Employee):
#     def __init__(self, name):
#         super().__init__(name, "Veterinarian")
#
#     def heal_animal(self, animal):
#         print(f"{self.name} лечит животное {animal.name}.")
#
# class Zoo:
#     def __init__(self, name):
#         self.name = name
#         self.animals = []
#         self.employees = []
#
#     def add_animal(self, animal):
#         self.animals.append(animal)
#         print(f"Добавлено животное: {animal}")
#
#     def add_employee(self, employee):
#         self.employees.append(employee)
#         print(f"Добавлен сотрудник: {employee}")
#
#     def list_animals(self):
#         print("Животные в зоопарке:")
#         for animal in self.animals:
#             print(f" - {animal}")
#
#     def list_employees(self):
#         print("Сотрудники зоопарка:")
#         for employee in self.employees:
#             print(f" - {employee}")
#
#     def save_to_file(self, filename):
#         data = {
#             "animals": [animal.to_dict() for animal in self.animals],
#             "employees": [employee.to_dict() for employee in self.employees]
#         }
#         with open(filename, 'w') as file:
#             json.dump(data, file)
#         print(f"Data saved to {filename}")
#
#     def load_from_file(self, filename):
#         try:
#             with open(filename, 'r') as file:
#                 data = json.load(file)
#             self.animals = [Animal.from_dict(animal_data) for animal_data in data["animals"]]
#             self.employees = [Employee.from_dict(employee_data) for employee_data in data["employees"]]
#             print(f"Data loaded from {filename}")
#         except FileNotFoundError:
#             print(f"File {filename} not found. Starting with an empty zoo.")
#         except json.JSONDecodeError:
#             print(f"Error decoding JSON from {filename}. Starting with an empty zoo.")
#
# zoo = Zoo("Городской Зоопарк")
#
# # Добавляем животных
# lion = Animal("Лев", "Пантеры")
# elephant = Animal("Слон", "Африканский слон")
# zoo.add_animal(lion)
# zoo.add_animal(elephant)
#
# # Добавляем сотрудников
# keeper = ZooKeeper("Анна")
# vet = Veterinarian("Иван")
# zoo.add_employee(keeper)
# zoo.add_employee(vet)
#
# # Выводим списки
# zoo.list_animals()
# zoo.list_employees()
#
# # Взаимодействие сотрудников с животными
# keeper.feed_animal(lion)
# vet.heal_animal(elephant)
#
# # Загрузка данных из файла
# zoo.load_from_file('zoo_data.json')
#
# # Сохранение данных в файл
# zoo.save_to_file('zoo_data.json')