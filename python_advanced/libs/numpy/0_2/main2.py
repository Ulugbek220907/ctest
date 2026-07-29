import pandas as pd
import numpy as np


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Department': ['Tech', 'Sales', None, 'HR'],          # Charlie is missing a department
    'Salary': [85000, None, 78000, 69000],                # Bob is missing salary
    'Join_Date': ['2020-01-15', '2021-03-22', '2019-11-05', '2022-07-01']
}

df = pd.DataFrame(data)
print(df)

