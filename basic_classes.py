class Vehicle:
    def __init__(self, make, model, speed):
        self.make = make
        self.model = model
        self.speed = speed
    def accelerate(self):
        self.speed += 10
        return f"Vehicle is now going at {self.speed} km/h!"
    def brake(self):
        self.speed -= 5
        return f"Vehicle slowed down to {self.speed} km/h!"
    def presentation(self):
        return f"Make: {self.make}| Model: {self.model}| Speed: {self.speed}"


truck = Vehicle("Mercedes Benz", "TZ100", 70)
print(truck.presentation())
print(truck.accelerate())
print(truck.accelerate())
print(truck.accelerate())
print(truck.brake())
print(truck.model)