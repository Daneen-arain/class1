from abc import ABC, abstractmethod


class Animal(ABC):

    
    @abstractmethod
    def move(self):
        pass

   
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):

    def move(self):
        print("I can walk and run")

    def make_sound(self):
        print("Woof! Woof!")

class Cat(Animal):

    def move(self):
        print("I can walk and jumpand run!!!" )

    def make_sound(self):
        print("Meow! Meow!")


def animal_sound(animal):
    animal.make_sound()

def animal_move(animal):
    animal.move()


dog = Dog()
cat = Cat()


animal_move(dog)
animal_sound(dog)

animal_move(cat)
animal_sound(cat)
