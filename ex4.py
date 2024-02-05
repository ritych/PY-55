class MeansOfTransport:
    def __init__(self, color, brand):
        self.__color = color
        self.__brand = brand

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand


def main():
    car = MeansOfTransport('green', 'Renault')
    print(car.brand)
    print(car.color)


if __name__ == "__main__":
    main()
