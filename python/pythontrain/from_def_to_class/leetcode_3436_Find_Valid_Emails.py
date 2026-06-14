import re
import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    regx = r"^[a-zA-Z]+@[a-zA-Z]+.com$"
    filtered_df = users[users['email'].str.contains(regx, regex=True)]
    # print(filtered_df)
    # result = users.copy()
    
    return filtered_df

user_data = [
    {'user_id': 1, 'email': 'alice@example.com'},
    {'user_id': 2, 'email': 'bob_at_example.com'},
    {'user_id': 3, 'email': 'charlie@example.net'},
    {'user_id': 4, 'email': 'david@domain.com'},
    {'user_id': 5, 'email': 'eve@invalid'},
]

users = pd.DataFrame(user_data)
# print(users)
getAnsw = find_valid_emails(users)
print(getAnsw)