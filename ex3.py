class MeansOfTransport:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def show_color(self):
        print(self.color)

    def show_brand(self):
        print(self.brand)


def main():
    car = MeansOfTransport('green', 'Renault')
    car.show_brand()
    car.show_color()


if __name__ == "__main__":
    main()
