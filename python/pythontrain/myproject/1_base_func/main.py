# class Animal:
#     def __init__(self, name, sounds):
#         self.name = name
#         self.sounds = sounds

#     def introduce(self):
#         return f"The {self.name} makes sound: {self.sounds}"
    
#     def walk(self):
#         raise NotImplementedError("need realise self function")

# class Dogs(Animal):
#     def __init__(self, name, sounds, walk):
#         super().__init__(name, sounds)
#         self.walked = walk
#         self.name = name
        
#     def walk(self):
#         return f"{self.name} walk on the {self.walked}"
#     # def introduce(self):
#     #     return f"{super().introduce()}"

# class Cats(Animal):
#     def __init__(self, name, sounds, enabled, walk):
#         super().__init__(name, sounds)
#         self.enabled = enabled
#         self.name = name
#         self.walked = walk

#     def introduce(self):
#         return f"{super().introduce()} is {self.enabled}" 
    
#     def walk(self):
#         deal = self.__whatisdoing()
#         return deal
#     def __whatisdoing(self):
#         return f"{self.name} walked on the {self.walked}"
    

# cats = Cats("Barsik", "Meow", "Mrrr..", "roof")

# name_dog = input("Whats is name of doggy: ")
# sounds = input(f"How sound a {name_dog}: ")
# walk = input(f"Where walk {name_dog} when {sounds}: ")

# dogs = Dogs(name_dog, sounds, walk)

# print(dogs.introduce())
# print(dogs.walk())
# print(cats.introduce())
# print(cats.walk())

# class BanksApp:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self._balance = balance

#     def _calculate_interest(self):
#         return self._balance * 0.05
    
#     def calculate_interest(self):
#         interest = self._calculate_interest()
#         self._balance += interest
#         return f"новый баланс {self._balance}"
    
    
#     def _minus_balance(self):
#         return self._balance - 5
    
#     def minus_balance(self):
#         get_balance = self._minus_balance()
#         return f"Операция вычитания: {get_balance}"
    
# account = BanksApp("Пётр", 1000)
# print(account.minus_balance())
# print(account.minus_balance())
# print(account.minus_balance())

class Animal():
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def introduce(self):
        return f"the animal name is {self.name}, he makes sounds: {self.sound}"
    
    def walk(self):
        raise NotImplementedError ("need realise self function")
    

class Dogs(Animal):
    def __init__(self, name, walk, sounds):
        super().__init__(name, sounds)
        self.walked = walk
        self.name = name

    def walk(self):
        return f"{self.name} walk on the {self.name}"
    
    def introduce(self):
        return super().introduce()
    
class Cats(Animal):
    def __init__(self, name, sounds, walk, enabled):
        super().__init__(name, sounds)
        self.name = name
        self.walked = walk
        self.enabled = enabled

    def introduce(self):
        return f"{super().introduce()} is {self.walked}"
    
    def walk(self):
        deal = self.__introduced()
        return deal
    def __introduced(self):
        return f"{self.name} walked on the {self.walked}"
    
cat = Cats("Barsik", "meow", "roof", "brbrbr")
print(cat.introduce())
print(cat.walk())

dog = Dogs()
print(dog.walk())