class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old!"


ed = Person("Eduardo", 34)
print(ed.talk())
bob = Person("Bob Burguer", 48)
print(bob.talk())