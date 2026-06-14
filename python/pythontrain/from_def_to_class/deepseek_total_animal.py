class Animal:
    total_animals = 0
    
    def __init__(self, name):
        self.name = name
        Animal.total_animals += 1

class Dog(Animal):
    total_dogs = 0  # свой счетчик
    
    def __init__(self, name, breed):
        super().__init__(name)
        Dog.total_dogs += 1  # увеличиваем свой
        self.breed = breed

class Cat(Animal):
    total_cats = 0  # свой счетчик
    
    def __init__(self, name, color):
        super().__init__(name)
        Cat.total_cats += 1  # увеличиваем свой
        self.color = color

# Создаем
dog1 = Dog("Рекс", "овчарка")
dog2 = Dog("Бобик", "дворняга")
cat1 = Cat("Мурка", "белая")

print(f"Всего животных: {Animal.total_animals}")  # 3
print(f"Собак: {Dog.total_dogs}")                # 2
print(f"Кошек: {Cat.total_cats}")                # 1