from ex4 import MeansOfTransport


class Moped(MeansOfTransport):
    def __init__(self, wheel, color, brand):
        super().__init__(color, brand)
        self.wheel = wheel

    @staticmethod
    def get_time(s, v):
        return s // v


moped = Moped(2, 'red', 'Kawasaki')
print(moped.get_time(100, 20))
