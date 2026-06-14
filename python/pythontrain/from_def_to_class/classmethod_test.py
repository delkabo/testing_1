class Animal:
    animal_count = 0
    count = 0
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        print(f"The animal {self.name} has created")
        self.__class__.count += 1
        # Animal.animal_count += 1
        print(f"Общее количество животных: {Animal.animal_count}")

    def hello(self):
        print(f"The {self.name} make sound {self.sound}")

    @classmethod
    def get_count(cls):
        # cls.count = 20
        print(f"Количество через classmethod: {cls.count}")

    @classmethod
    def reset_count(cls):
        cls.count = 0
        print(cls.count)

class Dog(Animal):
    # pass
    count = 0
    def __init__(self, name, sound, where_live):
        super().__init__(name, sound)         
    #  super().__init__(name, sound)
        self.name = name
        self.sound = sound
        self.where_live = where_live
        # self.__class__.count += 1
        # Dog.count += 1
        # print(f"Dogs count is {self.__class__.count}")

    def about(self):
    #     super().hello()
        print(f"The {self.name}. The sound is a {self.sound}. He lives at {self.where_live}")

    

testAnimal = Animal("Barsik", "meow")
testAnimal1 = Animal("Barsik1", "meow")
testAnimal2 = Animal("Barsik2", "meow")
# testAnimal.hello()
print("animal")
# testAnimal.get_count()
print("-------------")
zhuchka = Dog("Zhuchka", "Bark", "home")
polkan = Dog("Polkan", "Bark", "home")
zhuchka.about()
print("zhuchka")
zhuchka.get_count()
print("-------------")
# testAnimal.get_count()                                                                                                                                      
print("-------------")
print("zhuchka")
zhuchka.get_count()
print(f"Полкан {polkan.count}")
zhuchka.reset_count()
print("zhuchka")
zhuchka.get_count()
print("animal")
Animal.get_count()
print("------polkan------")
polkan.get_count()
print("------------")
print(Animal.animal_count)
