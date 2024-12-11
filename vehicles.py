# Base class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses should implement this!")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Testing polymorphism
def test_move(vehicle):
    vehicle.move()

# Creating instances
car = Car()
plane = Plane()

# Testing the polymorphism
test_move(car)  # Output: Driving 🚗
test_move(plane)  # Output: Flying ✈️
