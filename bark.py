class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof! Woof! I am", self.name, "and I am", self.age, "years old.")

    def woof(self):
        print("Woof! Woof! I am", self.name, "and I am", self.age, "years old.")

my_dog = Dog("Ali", 10)
my_dog1 = Dog("eshaal", 17)

my_dog.bark()
my_dog1.woof()