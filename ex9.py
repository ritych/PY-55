from ex4 import MeansOfTransport


class Car(MeansOfTransport):
    car_drive = 4

    def __init__(self, wheel, color, brand):
        super().__init__(color, brand)
        self.wheel = wheel

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __del__(self):
        pass

    def __getattr__(self, item):
        return False

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __delattr__(self, item):
        object.__delattr__(self, item)


car = Car(4, 'red', 'Kawasaki')

print(car.__dict__)