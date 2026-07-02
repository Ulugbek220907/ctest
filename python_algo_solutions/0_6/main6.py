

def func(x):
    if x == 0:
        return True
    elif x > 0:
        a = str(x)
        b = a[::-1]
        if int(a) == int(b):
            return True
        else:
            return False
    else:
        return False

print(func(0))