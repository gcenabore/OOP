class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        print("Animal's sound.")
    
    def describe(self):
        print(f"Animal named {self.name}, and Age: {self.age}")

def Lion(Animal):
    def make_sound(self):
        print("RAWR RAWR RAW!!!")
    
    def roar(self):
        print("ROARS Loudly.")

def Bird(Animal):
    def make_sound(self):
        print("CHIRP CHIRP CHIRP!!!")
    
    def fly(self):
        self("Flies high in the sky")

def Reptile(Animal):
    def make_sound(self):
        print("Hiss HIss HIss!!")
    
    def crawl(self):
        print("crawls silently, gumagapang skibidi.")

def main(): 
    lion = Lion("Leonellicactuselli", 10)
    bird = Bird("Bombombinigoosini", 5)
    reptile = Reptile("Bocanco", 2)

    for animal in [lion, bird, reptile]:
        animal.describe()
        animal.make_sound()
        print()
    
    lion.roar()
    bird.fly()
    reptile.crawl()

if __name__ == "__main__":
    main()