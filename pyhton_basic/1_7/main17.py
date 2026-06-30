#modules => libraries of functions and variables that can be used in your program.
#like math, random, os, sys, datetime, time, etc.

import math

#to import a specific function from a module, we can use the following syntax:
from math import sqrt

#or we can import our own custom module
import lib #importing a custom module

print(math.sqrt(16)) #using the module name to access the function
print(sqrt(25)) #using the function name directly after importing it
print(sqrt(27)) 
print(lib.add(5, 10)) #using a function from the custom module
