class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        return f"{self.name} says: Woof Woof"


dugger = Dog("Dugger")
print(dugger)