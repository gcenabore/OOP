class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        print("Animal's sound.")
    
    def describe(self):
        print(f"Animal named {self.name}, and Age: {self.age}")

