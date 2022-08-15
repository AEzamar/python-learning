class Dog:
    def __init__(self, name, age):
        self.name = name
    def info(self):
        return f"{self.name} is {self.age} years old!"
    def bark(self):
        return f"{self.name} says: Woof Woof"


dugger = Dog("Dugger", 7)
print(dugger)