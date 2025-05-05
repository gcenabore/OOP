class Animal: # Base class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        print("Animal's sound.")
    
    def describe(self):
        print(f"{self.__class__.__name__} named {self.name}, Age: {self.age}")

# Derived classes
class Lion(Animal):
    def make_sound(self):
        print("RAWR RAWR RAW!!!")
    
    def roar(self):
        print("ROARS Loudly.")


class Bird(Animal):
    def make_sound(self):
        print("CHIRP CHIRP CHIRP!!!")
    
    def fly(self):
        print("Flies high in the sky")


class Reptile(Animal):
    def make_sound(self):
        print("Hiss HIss HIss!!")
    
    def crawl(self):
        print("crawls stealthily, gumagapang skibidi.")

# testing the classes and polymorphism

def main(): #creating instances for the classes

    lion = Lion("Leonelli cactuselli", 10)
    bird = Bird("Bombombini goosini", 5)
    reptile = Reptile("El Bocanco Del Serpos", 2)
    
    # Call describe and make_sound (polymorphism)
    for animal in [lion, bird, reptile]:
        animal.describe()
        animal.make_sound()
        print()


     # call specific behaviors
    lion.roar()
    bird.fly()
    reptile.crawl()

if __name__ == "__main__": # Used to run the main function
    main()