import pandas as pd

df_employee_data = pd.read_csv('datasets/employee_data.csv')

df_employee = df_employee_data[['FirstName', 'LastName', 'StartDate', 'ExitDate', 'EmployeeType', 'DepartmentType' ,'GenderCode', 'Supervisor']].dropna()

df_employee.dtypes

df_employee['StartDate'] = pd.to_datetime(df_employee['StartDate'])
df_employee['ExitDate'] = pd.to_datetime(df_employee['ExitDate'])

df_employee['stayCompany']  = df_employee['ExitDate'] - df_employee['StartDate']

df_employee  = df_employee.sort_values(by='stayCompany', ascending=False)
