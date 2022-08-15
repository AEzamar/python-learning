class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return f"{self.name} is {self.age} years old!"
    def bark(self):
        return f"{self.name} says: Woof Woof"

class Cat(Dog):
    def meow(self):
        return f"{self.name} says: meow meow!"


dugger = Dog("Dugger", 7)
print(dugger)
print(dugger.info())
print(dugger.bark())

catmandu = Cat("Catmandu", 5)
print(catmandu)
print(catmandu.info())
print(catmandu.meow())