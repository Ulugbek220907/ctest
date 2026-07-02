#given two arrays, finding the median of merged array
def medianarray(arr1, arr2):
    arr = arr1 + arr2
    arr.sort()
    
    print(arr)
    n = len(arr)
    if n % 2 == 0:
        median = float(arr[n//2 - 1] + arr[n//2])
        median /= float(2)
    else:
        median = float(arr[n // 2])
    return median

a = 2
print(float(a))

print(medianarray([1, 2, 3, 5], [3, 4, 6, 7]))