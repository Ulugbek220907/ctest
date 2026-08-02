import pandas as pd

data = {
    'Department': ['Tech', 'Tech', 'Tech', 'Sales', 'Sales', 'HR', 'HR'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
    'Salary': [90000, 85000, 95000, 65000, 70000, 60000, 58000],
    'Experience_Years': [5, 3, 8, 2, 4, 1, 3]
}

df = pd.DataFrame(data)


# Group by 'Department' and calculate mean for 'Salary'
avg_salary_by_dept = df.groupby('Department')['Salary'].mean()
print(avg_salary_by_dept)