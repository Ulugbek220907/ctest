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

# Get count of employees AND average salary for each department
dept_summary = df.groupby('Department').agg(
    Employee_Count=('Employee', 'count'),
    Average_Salary=('Salary', 'mean'),
    Max_Experience=('Experience_Years', 'max')
)


# how much paid for each department
all = df.groupby('Department')['Salary'].sum()

# Count of employees in each department
b = df.groupby('Department')['Employee'].count()

###################################################

# Q1 regional sales team
q1_team = pd.DataFrame({
    'Employee': ['Alice', 'Bob'],
    'Sales': [15000, 18000]
})

# Q2 regional sales team
q2_team = pd.DataFrame({
    'Employee': ['Charlie', 'Diana'],
    'Sales': [22000, 19000]
})

# Stack them vertically (axis=0 is default)
combined_team = pd.concat([q1_team, q2_team], ignore_index=True)
print(combined_team)
