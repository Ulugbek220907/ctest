
def ts(nums):
    list1 = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if i != j and j != k and i != k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        list1.append([nums[i], nums[j], nums[k]])
    try:
        for i in range(len(list1)):
            list1[i].sort()
            if list1[i] in list1[:i]:
                list1.remove(list1[i])
    except IndexError:
        pass

    return list1

print(ts([0,0,0,0]))