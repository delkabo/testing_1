class car():
    number_of_cars = 0
    def __init__(self, model, power, doors):
        self.power = power
        self._doors = doors
        self.model = model
        self.__class__.number_of_cars += 1

    @staticmethod
    def summirize(value1, value2):
        value1 += value2
        return f"Summing two numbers: {value1}"


    @property
    def doors(self):
        return self._doors

    @doors.setter
    def doors(self, value):
        if isinstance(value, (int, float)):
            self._doors = value
        else:
            raise ValueError("Value mast be integer")

    def open_the_door():
        raise NotImplementedError("need raise self function")

    @classmethod
    def get_sum_cars(cls):
        return f"number_of_cars: {cls.number_of_cars}"

    @classmethod
    def reset_number_cars(cls):
        cls.number_of_cars = 0
        return cls.number_of_cars

    def presentation(self):
        return f"The {self.model}, have doors: {self._doors} and power: {self.power} horses"

class truck(car):
    number_of_cars = 0
    def __init__(self, model, power, doors, axels):
        super().__init__(model, power, doors)
        self.axels = axels

    def open_the_door(self):
        return "The door opened"



alfaromeo = car("alfa romeo", 300, 2)
alfaromeo = car("bmw", 320, 4)
print(alfaromeo.presentation())
print(alfaromeo.get_sum_cars())
print(alfaromeo.reset_number_cars())
print(alfaromeo.get_sum_cars())

print(alfaromeo.doors)
alfaromeo.doors = "ololo"
print("Number of cars volvo: " + str(alfaromeo.doors))

volvo = truck("volvo", 500, 2, 3)
print(volvo.presentation())
print(volvo.get_sum_cars())
print(volvo.reset_number_cars())
print(volvo.get_sum_cars())
print(volvo.open_the_door())
# print(volvo.doors)
# volvo.doors = 50
# print("Number of cars volvo: " + volvo.doors)

var1="dog want eat"
arr_var1 = var1.split()
print(arr_var1)