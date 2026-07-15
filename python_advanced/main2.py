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
list2 = [n if n > 0 else "Negative number" for n in list1]

temperatures = [-5, 12, 0, 35, 18, -2]
list3 = [n*1.8+32 if n > 0 else "freezing" for n in temperatures]

print(list3)