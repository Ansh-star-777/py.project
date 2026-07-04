from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def fuel_type(self):
        pass

    @abstractmethod
    def max_speed(self):
        pass


class BMW(Car):
    def fuel_type(self):
        print("BMW uses Petrol")

    def max_speed(self):
        print("BMW max speed is 250 km/h")


class Ferrari(Car):
    def fuel_type(self):
        print("Ferrari uses Petrol")

    def max_speed(self):
        print("Ferrari max speed is 340 km/h")


b = BMW()
f = Ferrari()

for car in (b, f):
    car.fuel_type()
    car.max_speed()
