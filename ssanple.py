import pandas as pd
import numpy as np

file_path = 'C:/Users/AAAAA/sample data/Employee Sample Data - Copy(4).xlsx'
df = pd.read_excel(file_path)

# Step 1: Data Cleaning
df.drop_duplicates(inplace=True)  # Remove duplicate rows
df.fillna({'Annual Salary': df['Annual Salary'].mean()}, inplace=True)  # Fill missing salary values with the mean
df['Age'] = df['Age'].fillna(df['Age'].mean()).astype(int)  # Fill missing ages with the mean and convert to integer

replacement_data = pd.DataFrame({
    'EEID': ['E10001', 'E10002', 'E10003', 'E10004', 'E10005'],
    'Full Name': ['John Doe', 'Jane Smith', 'Alice Johnson', 'Tom Brown', 'Emma Wilson'],
    'Job Title': ['Manager', 'Analyst', 'Engineer', 'Consultant', 'Developer'],
    'Department': ['HR', 'Finance', 'Engineering', 'Marketing', 'Sales'],
    'Business Unit': ['Corporate', 'Corporate', 'Engineering', 'Sales', 'Sales'],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
    'Ethnicity': ['Caucasian', 'African American', 'Asian', 'Hispanic', 'Caucasian'],
    'Age': [30, 25, 28, 32, 40],
    'Hire Date': pd.to_datetime(['2015-01-01', '2016-02-01', '2017-03-01', '2018-04-01', '2019-05-01']),
    'Annual Salary': [70000, 85000, 95000, 65000, 90000],
    'Bonus %': [0.10, 0.15, 0.20, 0.10, 0.15],
    'Country': ['United States', 'United States', 'United States', 'United States', 'United States'],
    'City': ['New York', 'Chicago', 'San Francisco', 'Los Angeles', 'Seattle'],
    'Exit Date': [pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT]
})

# Replace the first 5 rows in the original DataFrame
df.iloc[0:5] = replacement_data.values

# Display the modified DataFrame
print(df.head(10))


# Step 3: Print the row with the largest salary
highest_salary_row = df.loc[df['Annual Salary'].idxmax()]
print("Employee with the highest salary:")
print(highest_salary_row)

# Step 4: Group by department and calculate the average age and salary
department_group = df.groupby('Department').agg({'Age': 'mean', 'Annual Salary': 'mean'})
print("\nAverage Age and Salary by Department:")
print(department_group)

# Step 5: Group by department and ethnicity and find the maximum and minimum age, and median salary
dept_ethnicity_group = df.groupby(['Department', 'Ethnicity']).agg({
    'Age': ['max', 'min'],
    'Annual Salary': 'median'
})

print("\nMax Age, Min Age, and Median Salary by Department and Ethnicity:")
print(dept_ethnicity_group)

df.to_excel('C:/Users/AAAAA/sample data/cleaned_employee_data.xlsx', index=False)
