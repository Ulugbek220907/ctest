#OOP
#class and constructor

class Car:
    #class variable. accesible by all objects of the class
    x = 10

    #constructor
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    #method to display car information
    def display_info(self):
        print(f"Car Name: {self.name}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

#object creation
car1 = Car("Toyota", "Camry", 2020)
car1.display_info()


#inheritance: class that allows a class to inherit properties and methods from another class

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    #Dog class inherits from Animal class

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        return "Woof!"

class Cat(Animal):
    #Cat class inherits from Animal class

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speak(self):
        return "Meow!"

class Cow(Animal):
    #Cow class inherits from Animal class

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        return "Moo!"
