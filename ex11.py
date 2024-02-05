from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def voice(self):
        pass


class Cat(Animal):
    def voice(self):
        return "Meow"


cat = Cat()
cat_sound = cat.voice()
print(cat_sound)