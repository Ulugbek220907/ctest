"""
ternary in comprehension

simple ternary operator:
[if_condition_true if condition else if_condition_false]

EXAMPLE:
x = -10
a = True if x > 0 else False

OUTPUT:
False

but 

ternary in comprehension:
[if_condition_true if condition else if_condition_false for i in iterable]

EXAMPLE:
list1 = [-1, 2, 3, -4, 5, -6]
list2 = [i if i > 0 else "Negative number" for i in list1]

OTPUT:
['Negative number', 2, 3, 'Negative number', 5, 'Negative number']


ishqilib listdagi barcha elementlar qoladi, lekin shu xolat(condition)ga mos tushmagan
elementlarga o'zgartirish kirg'azamiz, easy

"""


list1 = [-1, 2, 3, -4, 5, -6]
list2 = [i if i > 0 else "Negative number" for i in list1]
print(list2)