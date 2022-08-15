class Mammal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return f"{self.name} is {self.age} years old!"
    

class Dog(Mammal):
    def bark(self):
        return f"{self.name} says: Woof Woof"


class Cat(Mammal):
    def meow(self):
        return f"{self.name} says: meow meow!"


class Ferret(Mammal):
    def stuff(self):
        return f"{self.name} says: *Ferret noises*"


class GuineaPig:
    pass


dugger = Dog("Dugger", 7)
print(dugger)
print(dugger.info())
print(dugger.bark())
catmandu = Cat("Catmandu", 5)
print(catmandu)
print(catmandu.info())
print(catmandu.meow())
long_dude = Ferret("Long Dude", 4)
print(long_dude)
print(long_dude.info())
print(long_dude.stuff())