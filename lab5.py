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
    lion = Lion("Leonelli Cactuselli", 10)
    bird = Bird("Bombombini goosini", 5)
    reptile = Reptile("El Bocanco Del Serpos", 2)

