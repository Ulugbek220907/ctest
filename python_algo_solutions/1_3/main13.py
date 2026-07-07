def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    b = 0
    target += 1
    list1 = []
    for i in range(len(candidates)):
        a = 0
        b = 0
        list2 = []
        for j in range(i + 1, len(candidates)):
            list2.append(candidates[j])
            b += candidates[j]
            a = candidates[i] + b
            print(a)
            if a == target:
                list2.append()
            else:
                list2.clear()
            print(list2)
        if list2 == []:
            continue
        else:
            list1.append(list2)
    print(list1)
    

combinationSum([2,3,6,7], 7)
