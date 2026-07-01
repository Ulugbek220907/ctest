#OOP
#class and constructor
#polymorphosm and inheritance

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
        super().__init__(name) #super() is used to call the constructor of the parent class
        self.breed = breed

    def speak(self):
        return "Woof!"

class Cat(Animal):
    #Cat class inherits from Animal class

    def __init__(self, name, color):
        #polymorphism: same method name but different implementation in different classes
        super().__init__(name)
        self.color = color

    def speak(self):
        return "Meow!"

class Cow(Animal):
    #Cow class inherits from Animal class

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Moo!"

#object creation
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Tabby")
cow = Cow("Bessie", "Holstein")

#displaying information
print(f"{dog.name} says {dog.speak()}")
print(f"{cat.name} says {cat.speak()}")
print(f"{cow.name} says {cow.speak()}")