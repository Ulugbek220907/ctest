#slicing

arr = [12, 34, 56, 89, 102, 43, 87, 54, 21, 9]

# we can get first and last element of the array
first, *mid, last = arr 

print(first)
print(mid)
print(last)

#reversing the list
# [start:stop:end]

reversed_list = arr[::-1]

print(reversed_list)


