class Person:
    def __init_(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
    def intro(self):
        print(f"Hello, my name is {self.name}, I\'m {self.age} years old and I\'m a {self.job}")


ed = Person("Eduardo", 34, "Software Developer")
print(ed)
ed.intro()

