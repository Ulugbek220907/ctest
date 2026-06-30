#collection = single variable used to store multiple values in a single variable
# list = [1,2,3,4,5] ordered, changeable, allows duplicate members
# set = {1,2,3,4,5} unordered, unchangeable, no duplicate members
# tuple = (1,2,3,4,5) ordered, unchangeable, allows duplicate members
# dictinonary = {"name": "John", "surname": "Doe", "age": 30, "height": 1.75} ordered, changeable, no duplicate members

list1 = [1, 2, 3, 4, 5]
set1 = {1, 2, 3, 4, 5}
tuple1 = (1, 2, 3, 4, 5)
dic = {
    "name": "John",
    "surname": "Doe",
    "age": 30,
    "height": 1.75
}

#adding elements to the collections
list1.append(6) #adding an element to the list
set1.add(6) #adding an element to the set
tuple1 = tuple1 + (6,) #adding an element to the tuple
dic["weight"] = 70 #adding a key-value pair to the dictionary

#dictionary methods
dic.update({"weight": 75}) #updating the value of the "weight" key
dic.pop("weight") #removing the "weight" key-value pair from the dictionary
dic.clear() #removing all key-value pairs from the dictionary
dic.copy() #creating a copy of the dictionary
dic.popitem() #removing the last key-value pair from the dictionary
keys = dic.keys() #returning a list of all the keys in the dictionary - name, surname, age, height
values = dic.values() #returning a list of all the values in the dictionary - John, Doe, 30, 1.75
items = dic.items() #returning a list of all the key-value pairs in the dictionary - ("name", "John"), ("surname", "Doe"), ("age", 30), ("height", 1.75) as tuples
a = dic.get("name") #returning the value of the "name" key in the dictionary - John

for i in list1:
    print(i) #accessing all elements of the list

print(list1[0]) #accessing the first element of the list
print(tuple1[0]) #accessing the first element of the tuple

print(list1) #accessing the list
print(set1) #accessing the set
print(tuple1) #accessing the tuple

print(dic["name"]) #accessing the value of the "name" key in the dictionary
print(dic["surname"]) #accessing the value of the "surname" key in the dictionary
print(dic["age"]) #accessing the value of the "age" key in the dictionary
print(dic["height"]) #accessing the value of the "height" key in the dictionary
print(dic["weight"]) #accessing the value of the "weight" key in the dictionary