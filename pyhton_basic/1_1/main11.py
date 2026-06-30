#for loop = execute a block of code a limited amount of times
import time

my_time = int(input("Enter a number: "))

for x in range(my_time):
    print(x+1)
    time.sleep(1) #sleep() = delay the program for a number of seconds

for x in reversed(range(1, 11)): #range(satrt, stop, step) and reversed() reverse the order of the range
    print(x)