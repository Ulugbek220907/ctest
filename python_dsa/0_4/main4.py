#hash map = dict


dict1 = {
    "name" : "ulugbek",
    "age" : 19,
    "city" : "Tashkent",
    "year" : 2026
}

#methods of dict

#############################################
#viewing anf retrieving data from dict

#get() - returns the value of the specified key
print(dict1.get("name")) #ulugbek
print(dict1.get("age")) #19
print(dict1.get("city")) #Tashkent
print(dict1.get("year")) #2026

#keys() - returns a list of all the keys in the dictionary
print(dict1.keys()) #dict_keys(['name', 'age', 'city', 'year'])

#values() - returns a list of all the values in the dictionary
print(dict1.values()) #dict_values(['ulugbek', 19, 'Tashkent', 2026])

#items() - returns a list of tuples, each containing a key-value pair
print(dict1.items()) #dict_items([('name', 'ulugbek'), ('age', 19), ('city', 'Tashkent'), ('year', 2026)])

##############################################
#Adding and updating data in dict

#update() - updates the dictionary with the specified key-value pairs
dict1.update({"name" : "John", "age" : 25})
print(dict1) # {'name': 'John', 'age': 25, 'city': 'Tashkent', 'year': 2026}

#setdefault() - returns the value of the specified key. If the key does not exist, it inserts the key with the specified value
dict1.setdefault("country", "Uzbekistan")
print(dict1) # {'name': 'John', 'age': 25, 'city': 'Tashkent', 'year': 2026, 'country': 'Uzbekistan'}

#remove() - removes the specified key and its corresponding value from the dictionary
dict1.pop("year")

#popitem() - removes the last inserted key-value pair from the dictionary
dict1.popitem()

#clear() - removes all the key-value pairs from the dictionary
dict1.clear()


#copy and create dict

#copy() - returns a shallow copy of the dictionary

dict2 = dict1.copy()

#fromkeys() - creates a new dictionary with the specified keys and values
dict3 = dict.fromkeys(["name", "age", "city"], "unknown")

print(dict3) # {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}


print("---------------------------------------------------")
print("word frequency counter")
print("---------------------------------------------------")
sentence = input("Enter a sentence: ")

word = sentence.split(" ")

dict4 = {}

for i in range(len(word)):
    if word[i] not in dict4:
        a = 1
        dict4.setdefault(word[i], a)
    else:
        dict4[word[i]] += 1

print(dict4)




