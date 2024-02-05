from ex4 import MeansOfTransport


class Car(MeansOfTransport):
    def __init__(self, wheel, color, brand):
        super().__init__(color, brand)
        self.wheel = wheel


class Moped(MeansOfTransport):
    def __init__(self, wheel, color, brand):
        super().__init__(color, brand)
        self.wheel = wheel


car = Car(4, 'green', 'Renault')
moped = Moped(2, 'red', 'Kawasaki')
print(car.color)
print(moped.brand)
