# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Child classes with different implementations of move()
class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky")

class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing on the water")

class Bike(Vehicle):
    def move(self):
        print("🚴 Pedaling along the path")


# ---- TESTING ----
vehicles = [Car(), Plane(), Boat(), Bike()]

for v in vehicles:
    v.move()   # Polymorphism in action
