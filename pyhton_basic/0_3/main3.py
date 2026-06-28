#typecasting  => converting variables str(), int(), float(), bool()
#type() to check the type of variable


name = "John"
age = 30
gpa = 3.5
is_student = True

age = str(age)  # Convert integer to string
gpa = int(gpa)  # Convert float to integer
is_student = str(is_student)  # Convert to string

print(type(age))  # Output: <class 'str'>
print(type(gpa))  # Output: <class 'int'>
print(type(is_student))  # Output: <class 'str'>

print(is_student)  # Output: True