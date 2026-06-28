#input() => function that allows user to input data from the console
#returns a string value

import string

name = str(input("Enter your name: ")) #str
age = int(input("Enter your age: ")) #int and for boolean bool() and float() for float

print(f"Hello, {name}! You are {age} years old.")


width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

area = width * height

print(f"The area of the rectangle is: {area} cm²")

