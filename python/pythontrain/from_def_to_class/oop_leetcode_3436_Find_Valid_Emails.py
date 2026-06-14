import re
import pandas as pd

class ValidEmails():
    filtered_df = None
    def __init__(self, users: pd.DataFrame):
        self.users = users
        self.regx = r"^[a-zA-Z]+@[a-zA-Z]+.com$"
        # self.filtered_df = None

    def find_valid_emails(self):
        ValidEmails.filtered_df = self.users[self.users['email'].str.contains(self.regx, regex=True)]
        return self

    def print_result(self) -> pd.DataFrame:
        print(ValidEmails.filtered_df)
        # return ValidEmails.filtered_df


# def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
#     regx = r"^[a-zA-Z]+@[a-zA-Z]+.com$"
#     filtered_df = users[users['email'].str.contains(regx, regex=True)]
#     # print(filtered_df)
#     # result = users.copy()
    
#     return filtered_df

user_data = [
    {'user_id': 1, 'email': 'alice@example.com'},
    {'user_id': 2, 'email': 'bob_at_example.com'},
    {'user_id': 3, 'email': 'charlie@example.net'},
    {'user_id': 4, 'email': 'david@domain.com'},
    {'user_id': 5, 'email': 'eve@invalid'},
]

users = pd.DataFrame(user_data)
# print(users)
getAnsw = ValidEmails(users)
getAnsw.find_valid_emails().print_result()