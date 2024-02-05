from ex4 import MeansOfTransport


class Car(MeansOfTransport):
    car_drive = 4

    def __init__(self, wheel, color, brand):
        super().__init__(color, brand)
        self.wheel = wheel

    @classmethod
    def get_wheel(cls):
        print(cls.car_drive)


car = Car(4, 'red', 'Kawasaki')
car.get_wheel()
