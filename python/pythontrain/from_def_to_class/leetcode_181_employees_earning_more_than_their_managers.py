import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    print()
    # Создать копию таблицы и копию столбцов
    employee_copy = employee.copy()
    merge_table = pd.merge(
        employee, 
        employee_copy, 
        left_on='managerId', 
        right_on='id', 
        how='left', 
        suffixes=('_emp','_mang')
        )
    
    result = merge_table[merge_table['salary_emp'] > merge_table['salary_mang']]
    result_slice = result.reindex(columns=['name_emp'])
    result_slice = result_slice.rename(columns={'name_emp': 'Employee'})
    return(result_slice)

employee_data = [
    {"id": 1, "name": "Joe", "salary": 70000, "managerId": 3},
    {"id": 2, "name": "Henry", "salary": 80000, "managerId": 4},
    {"id": 3, "name": "Sam", "salary": 60000, "managerId": None},
    {"id": 4, "name": "Max", "salary": 90000, "managerId": None}
]

employee = pd.DataFrame(employee_data)
getAnsw = find_employees(employee)
print(getAnsw)