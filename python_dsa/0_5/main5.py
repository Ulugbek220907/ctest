#hash sets

#duplicates removed automatically
#no orders


unique_ids = {101, 102, 103, 104, 105}

#methods = add, remove, discard, pop, clear, union, intersection, difference

#add = adds elements to the set
#remove = removes elements from the set, raises error if element not found
#discard = removes elements from the set, does not raise error if element not found
#pop = removes and returns an arbitrary element from the set, raises error if set is empty
#clear = removes all elements from the set


set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union (all unique elements) shows all unique elements from both sets
print(set_a | set_b)   #output: {1, 2, 3, 4, 5} 

# Intersection (common elements) both sets have this element
print(set_a & set_b)   #output: {3}

# Difference (elements in set_a but not in set_b)
print(set_a - set_b)   #output: {1, 2}


def duplicate(l1):
    l2 = {}
    l2 = set(l1)
    if l2 == l1:
        return True
    else:
        return False

print(duplicate({1, 2, 3, 1}))




