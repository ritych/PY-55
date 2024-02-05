class Point:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, x, y):
        print('init')
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x, self.y


def main():
    pt = Point(1,2)

    print(pt.__dict__)


if __name__ == "__main__":
    main()
