#functions = blocks of code that perform a specific task


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

#positional function = strictly needs values
def addition(x, y):
    return x + y

#default function = if values are not provided, it will take default values
def addition2(x = 0, y = 0):
    return x + y

#keyword function method
r = addition(x=a, y=b) #order doesn't matter 

#arbitrary function method. it has *args and **kwargs. 
# *args is used for arbitrary number of positional arguments and **kwargs is used for arbitrary number of keyword arguments

#args
def addition3(*args): #args becomes a tuple and we can work with it as a tuple. * unpacking operator
    total = 0
    for i in args:
        total += i
    return total

#kwargs
def addition4(**kwargs): #kwargs becomes a dictionary and we can work with it as a dictionary. ** unpacking operator
    total = 0
    for key, value in kwargs.items():
        total += value
    return total

result = addition(a, b)
result2 = addition2(a)
result3 = addition3(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result4 = addition4(x=1, y=2, z=3)
print(a, "+", b, "=", result)

print(a, "+", b, "=", result2)
print("Arbitrary sum:", result3)