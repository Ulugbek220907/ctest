import pandas as pd


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [28, 34, 22, 31],
    'Department': ['Tech', 'Sales', 'Tech', 'HR'],
    'Salary': [85000, 62000, 78000, 69000]
}
df = pd.DataFrame(data)

print(df.loc[:, ('Salary', 'Age')])
list = df[df['Age'] < 30]
print(list)