#Stack using list, very ezzzz

def push(list1, data):
    list1.insert(0, data)

def pop(list1):
    list1.pop(0)

def isempty(list1):
    return True if len(list1) == 0 else False

def size(list1):
    return len(list1)

def peek(list1):
    return list1[0]

mylist = [1, 2, 3, 4, 5]

push(mylist, 12)
push(mylist, 33)

pop(mylist) #removed 33

print(mylist)
