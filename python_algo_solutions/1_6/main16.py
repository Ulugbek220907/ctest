

def permute(nums):
    list1 = []
    for i in range(len(nums)):
        list2 = []
        for k in range(len(nums)):
            list2.append(nums[k])
        list1.append(list2)
    print(list1)

permute([1,2,3])
    