import os 
import json

#file detection
file_path = "D:\\C proj\\0_1\\pyhton_basic\\2_4\\text.txt"
file_path_json = "D:\\C proj\\0_1\\pyhton_basic\\2_4\\text2.json"

if os.path.exists(file_path):
    print(f"The file '{file_path}' exists.")

else:
    print(f"The file '{file_path}' does not exist.")

if os.path.exists(file_path_json):
    print(f"The file '{file_path_json}' exists.")

else:
    print(f"The file '{file_path_json}' does not exist.")

employee1 = {
    "name": "John Doe",
    "age": 30,
    "position": "Software Engineer"
}

employee2 = {
    "name": "Jane Smith",
    "age": 25,
    "position": "Product Manager"
}

list_of_employees = [employee1, employee2]
list_output = []

#writing to a file with exception handling
try:
    #writing to json file
    with open(file_path_json, 'w') as file:
        json.dump(list_of_employees, file, indent=4)

    """
    writing to text file
    with open(file_path, 'w') as file:
        for employee in list_of_employees:
            for key, value in employee.items():
                file.write(f"{key}: {value}\n")
    print(f"Employee data has been written to '{file_path}'.")
    """

except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

try:
    #reading from json file
    with open(file_path_json, 'r') as file:
        data = json.load(file)
        print("Employee data read from JSON file:")
        print(data)
        #appending the data read from the JSON file to the list_output
        list_output.append(data)

    """
    reading from text file
    with open(file_path, 'r') as file:
        content = file.read()
        print("Employee data read from text file:")
        print(content)
    """
except Exception as e:
    print(f"An error occurred while reading from the file: {e}")

#printing the list of employees read from the JSON file
print("List of employees read from JSON file:")
for employee in list_output:
    print(employee)
