#enumerator in loops
array = ["apple", "banana", "cherry"]

for i in range(len(array)):
    print(f"Rank {i + 1}: ", array[i])


for rank, item in enumerate(array, start=1):
    print(f"Rank {rank}: {item}")

status_codes = [200, 201, 404, 200, 500, 301, 403]

list1 = [(f"Request {rank} failed with status {code}") for rank, code in enumerate(status_codes, start=1) if code >= 400]

print(list1)