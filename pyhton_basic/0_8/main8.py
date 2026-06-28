#indexing operators = accesing elements of a string [start:end:step]

fullname = "John Doe is good guy"

print(fullname[0]) #J          first character of the string
print(fullname[1]) #o          second character of the string
print(fullname[0:2]) #Jo       first two characters of the string
print(fullname[2:5]) #hn Doe   from the third character to the end of the
print(fullname[3:6]) #n D      from the fourth character to the sixth character of the string
print(fullname[::2]) #Jh o     every second character of the string
print(fullname[::-1]) #yaug doog si eoD nhoJ  reverses the string
print(fullname[-4:-1]) # gu    last three characters of the string


