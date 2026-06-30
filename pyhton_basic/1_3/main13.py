#random numbers, or any randomness

import random

floatnumber = random.random() #random() = return a random float between 0.0 and 1.0
number = random.randint(1, 10) #randint(start, stop) = return a random integer between the two numbers

#random methods

randomlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


random.seed(1) #seed() = initialize the random number generator with a seed value
random.shuffle(randomlist) #shuffle() = shuffle the elements of a list in place
choice = random.choice(randomlist) #choice() = return a random element from a list
random.sample(range(1, 100), 10) #sample(population, k) = return a list of k unique random elements from the population sequence
random.uniform(1, 10) #uniform(start, stop) = return a random float between the two numbers
random.randrange(1, 10, 2) #randrange(start, stop, step) = return a random integer from the range with the specified step
random.getrandbits(8) #getrandbits(k) = return a random integer with k random bits


randomlist = random.sample(range(1, 100), 10) #sample(population, k) = return a list of k unique random elements from the population sequence

print(f"Random float is: {floatnumber:.2f}") #:.2f = format the float to 2 decimal places
print(f"Random number is: {number}")
print(f"Random list is: {randomlist}")
