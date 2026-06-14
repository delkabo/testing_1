
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def present(self):
        return f"The {self.name} make sound {self.sound}....."
        return "---"
    
    def test(self):
        raise NotImplementedError("need make self function for class")

class Dog(Animal):
    def __init__(self, name, sound, live):
        super().__init__(name, sound)
        self.live = live
    
    def test(self):
        return f"He is live at {self.live}"
        return self.__hidefunc()

    def __hidefunc(self):
        return "ololo"


rex = Dog("Rex", "gav", "home")
print(rex.present())
# print(rex.present())
print(rex.test())


    