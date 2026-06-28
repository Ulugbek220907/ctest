#if elif else statements
#logical operators: and, or, not

a = int(input("Enter a number: "))

if a > 10:
    print("a is greater than 10")
elif a == 10:
    print("a is equal to 10")
else:
    print("a is less than 10")


b = str(input("Enter a string: "))

if b == "hello":
    print("You entered 'hello'")
else:
    print("You did not enter 'hello'")



c = int(input("Enter another number: "))

if c > 0 and c < 10:
    print("c is between 0 and 10")
elif c < 0 or c > 10:
    print("c is less than 0 or greater than 10")
else:
    print("c is equal to 0 or 10")