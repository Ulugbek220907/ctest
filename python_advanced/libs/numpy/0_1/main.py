import numpy as np


new_list = np.array([1,2,3,4,5])

# in numpy lib if we add a number to an array it will add for each element of the array
# [1, 2, 3] + 8 = [9, 10, 11]

newer_list = new_list + 8

#[1 2 3 4 5]        new_list
#[ 9 10 11 12 13]   newer_list

#methods in numpy lib

#max()     maximum
#min()     minimum
#mean()    average
#reshape() change the shape of the array
#shape     shape of the array, (rows, columns)
#ndim      dimension of the array



##################################################################

#2d array

grades = np.array([
    [85, 90, 78, 92],  # Student 0
    [88, 76, 95, 89],  # Student 1
    [70, 82, 80, 75]   # Student 2
])

# grades.shape => returns (3, 4) = (rows, columns)

# grades.ndim => dimension of the array (returns 2)

#returns the mean of each column
# [81. 83. 84. 85.]

#returns the mean of each row
# [86. 87. 77.]

# grades[1,:] returns the second (index 1) row of the array

numbers = np.array([12, 45, 67, 88, 23, 90, 34, 51])

new_nums = numbers[numbers > 40]

numbers = numbers.reshape(4, 2)  # reshapes the array to 4 rows and 2 columns
print(numbers)
