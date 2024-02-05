from ex4 import MeansOfTransport


class Car(MeansOfTransport):
    arg1 = 1
    _arg2 = 2
    __arg3 = 3

    def __init__(self, wheel, color, brand):
        super().__init__(color, brand)
        self.wheel = wheel


car = Car(4, 'red', 'Kawasaki')

print(car.arg1)
print(car._arg2)
print(car.__arg3)