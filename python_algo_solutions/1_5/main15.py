

def searchinsertpos(nums, target):

    k = 0
    
    for i in nums:
        if i >= target:
            break
        else:
            k += 1
    return k

print(searchinsertpos(nums = [1,3,5,6], target = 7))
