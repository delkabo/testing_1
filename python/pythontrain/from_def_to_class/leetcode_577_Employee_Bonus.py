import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merge_table = pd.merge(
                    employee,
                    bonus, 
                    on="empId", 
                    how="left")
    
    merge_table["bonus"] = merge_table["bonus"].fillna(0)
    result = merge_table[merge_table["bonus"] < 1000]
    result = result.reindex(columns=["name", "bonus"])
    result["bonus"] = result["bonus"].replace(0, None)
    return result

employee_data = [
    { "empId": 3, "name": "Brad", "supervisor": None, "salary": 4000  },
    { "empId": 1, "name": "John",  "supervisor": 3, "salary": 1000 },
    { "empId": 2, "name": "Dan",  "supervisor": 3, "salary": 2000  },
    { "empId": 4, "name": "Thomas",  "supervisor": 3, "salary": 4000 }
]

bonus_data = [
    {"empId": 2, "bonus": 500},
    {"empId": 4, "bonus": 2000}
]

employee = pd.DataFrame(employee_data)
bonus = pd.DataFrame(bonus_data)

GetAnsw = employee_bonus(employee, bonus)
print(GetAnsw)

