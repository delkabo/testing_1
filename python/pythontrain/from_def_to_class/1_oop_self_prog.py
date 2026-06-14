class Cars():
    count_cars = 0
    def __init__(self, brand, cost):
        self._brand = brand
        self._cost = cost
        self.__class__.count_cars += 1

    @property
    def cost(self):
        return f"test {self._cost}"

    @cost.setter
    def cost(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("value must be is integer or float")
        self.cost = value
        

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        # if value is None:
        #     raise ExceptionType("Field is empty")
        self._brand = value

    @classmethod
    def get_count(cls):
        print(cls.count_cars)

    @classmethod
    def reset_count(cls):
        cls.count_cars = 0
        return cls.count_cars


class Trucks(Cars):
    count_cars = 0
    def __init__(self, brand, cost, number_of_axes):
        super().__init__(brand, cost)
        self._number_of_axes = number_of_axes

    @property
    def number_of_axes(self):
        print(f"Количество осей: {self._number_of_axes}")

    @number_of_axes.setter
    def set_axes(self, value):
        if isinstance(value (int, float)):
            self._number_of_axes = value
        else:
            raise TypeError("Is not correst type of value. Need enter type or float.")

    # @staticmethod
    # def check_num(self, value):
        

peugeot = Cars("peugeot", 1000)
print(peugeot.brand)
peugeot.brand = "Ferrari"
print(peugeot.brand)
print(peugeot.count_cars)

alfaromeo = Cars("alfaromeo", 1200)
alfaromeo.get_count()
Cars.get_count()

optimus_prime = Trucks("prime", 3000, 8)
print(optimus_prime.brand)
optimus_prime.get_count()
print(optimus_prime.cost)