# @property = it is like getter method
# _variable  = variable is private and can only be accessed within the class



class Rectangle:
    #constructor 
    def __init__(self, width, height):
        self._width = width
        self._height = height

    #accessing protected variable and finding area and perimeter
    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)
    
    
    

rectangle1 = Rectangle(5, 10)

print(f"Area: {rectangle1.area}")  # Accessing area property
print(f"Perimeter: {rectangle1.perimeter}")  # Accessing perimeter property

rectangle1.width = 13
rectangle1.height = 7