class Car(object):
    count_cars = 0
    def __init__(self, wheels, type_body, wheight):
        self._wheels = wheels
        self._type_body = type_body
        self._wheight = wheight
        self.__class__.count_cars += 1

    def print_wheels(self):
        print(self._wheels)

    def print_type_body(self):
        print(self._type_body)

    def print_wheight(self):
        print(self._type_body)

    @property
    def wheels(self):
        return self._wheels
    
    @wheels.setter
    def wheels(self, value):
        self._wheels = value

    @property
    def type_body(self):
        return self._type_body

    @type_body.setter
    def type_body(self, value):
        if not isinstance(value, str):
            raise TypeError("Value should be is string")
        self._type_body = value

    @property
    def wheight(self):
        return self._wheight

    @wheight.setter
    def wheight(self, value):
        if not isinstance(value, int):
            raise TypeError("Value should be is a integer")
        self._wheight = value

    @classmethod
    def get_count_cars(cls):
        return cls.count_cars
    @classmethod
    def reset_count_cars(cls):
        cls.count_cars = 0
    @classmethod
    def return_cls(cls):
        return cls

class LightCars(Car):
    count_cars = 0
    def __init__(self, wheels, wheight, type_body, tunning):
        super().__init__(wheels, wheight, type_body)
        self._tunning = tunning

    @property
    def tunning(self):
        return self._tunning

    @tunning.setter
    def set_tunning(self, value):
        if not isinstance(value, str):
            raise TypeError("Value should be is string")
        self._tunning = value



new_car = Car(4, "heavy", 4000)
new_car.print_wheels()
new_car.print_type_body()
print(new_car.wheels)
new_car.wheels = 6
print(new_car.wheels)
new_car.get_count_cars()

new_car_1 = Car(4, "heavy", 4000)
new_car.get_count_cars()

new_car_3 = LightCars(4, "heavy", 4000, "super")
new_car_3.set_tunning = "super-puper"
print(new_car_3.tunning)
print(new_car_3.count_cars)
print(f"new_car_3: {new_car_3.get_count_cars()}")
new_car_4 = LightCars(4, "heavy", 4000, "super")
new_car_4.set_tunning = "super-puper"
print(new_car_4.tunning)
print(new_car_4.count_cars)
print(f"new_car_1: {new_car_1.get_count_cars()}")
print(f"new_car_4: {new_car_1.return_cls()}")
print(f"new_car_3: {new_car_3.get_count_cars()}")
print(f"new_car_4: {new_car_4.get_count_cars()}")
new_car_3.reset_count_cars()
print(f"new_car_4: {new_car_4.get_count_cars()}")
print(f"new_car_4: {new_car_4.return_cls()}")
