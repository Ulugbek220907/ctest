import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Department': ['Tech', 'Sales', None, 'HR'],          # Charlie is missing a department
    'Salary': [85000, None, 78000, 69000],                # Bob is missing salary
    'Join_Date': ['2020-01-15', '2021-03-22', '2019-11-05', '2022-07-01']
}

df = pd.DataFrame(data)

# .dropna() removes rows with any missing values
clean_df = df.dropna()


# .fillna() fills the missing values with a specified value
filled_df = df['Salary'].fillna(df['Salary'].mean())  # Fill missing salaries with the mean salary

# adds new column 
# df['ColumnName] = 'Value'
df['Status'] = 'Active'
df = df.drop(columns='Status')

df['Join_Date'] = pd.to_datetime(df['Join_Date'])

df['Salary'] = df['Salary'].fillna(int(df['Salary'].mean()))



df['Bonus'] = df['Salary'] * 0.1

df['Overall'] = df['Salary'] + df['Bonus']


print(df)