# class Person: #Parent Class
#     def __init__(self, firstname, lastname, age):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age

#     def print_name(self):
#         print(f"Name: {self.firstname} {self.lastname}, Age: {self.age}")
# Human = Person("John", "Doe", 30)


# class Student(Person): #Child Class
#     pass
# student = Student("Jane", "Doe", 20)


# student.print_name()
# Human.print_name()

# class Parent:
#     def __init__(self, parent_name):
#         self.parent_name = parent_name
#         print(f"Parent's name: {self.parent_name}")
#     def can_sing(self):
#         print(f"{self.parent_name} can sing!")

# class Child(Parent):
#     def __init__(self, parent_name, child_name):
#         super().__init__(parent_name)
#         self.child_name = child_name
#         print(f"child's name: {self.child_name}")
#         super().can_sing()

# x = Child("Marc", "Mercado")


#single inheritance

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("Can Speak!")
        pass

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        print(f"Dog's name: {self.name}, Age: {self.age}")

    def speak(self):
        super().speak()
        return "woof! woof!"
    
d = Dog("Max", 5)
print(d.speak())
