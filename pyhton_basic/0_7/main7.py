#string methods


name = input("Enter your name: ")
lenghth = len(name) #length method
findmethod = name.find("a") #finds the FIRST occurrence of the letter "a" in the string
uppermethod = name.upper() #converts the string to uppercase
capital = name.capitalize() #converts the FIRST character of the string to uppercase
lowermethod = name.lower() #converts the string to lowercase
digit = name.isdigit() #checks if the string contains only digits
alpha = name.isalpha() #checks if the string contains only letters not even spaces
counter = name.count("a") #counts the number of occurrences of the letter "a" in the string
replacing = name.replace("a", "e") #replaces all occurrences of the letter "a" with the letter "e"

print(lowermethod)