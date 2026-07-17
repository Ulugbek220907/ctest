#converting 2D arrays to 1D
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


flat = [k for i in matrix for k in i]
print(flat)