class Dog:

    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

    def display(self):
        print("Animal :", Dog.animal)
        print("Breed  :", self.breed)
        print("Colour :", self.colour)
        print()

dog1 = Dog("Golden Retriever", "Golden")
dog2 = Dog("German Shepherd", "Black and Tan")

print("Dog 1 Details")
dog1.display()

print("Dog 2 Details")
dog2.display()
