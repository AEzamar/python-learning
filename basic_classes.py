class Vehicle:
    def __init__(self, make, model, speed):
        self.make = make
        self.model = model
        self.speed = speed
    def accelerate(self):
        self.speed += 10
        return f"Vehicle is now going at {self.speed} km/h"


truck = Vehicle("Mercedes Benz", "TZ100", 70)
print(truck.accelerate())