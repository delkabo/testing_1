import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    print(person)
    print("-----------")
    min_ids = person.groupby('email')['id'].transform('min')
    # person.drop(person[person['id'] != min_ids].index, inplace=True)
    print(min_ids)
    print("-----------")
    # print(person)

person_data = [
    {'id': 1, 'email': 'john@example.com'},
    {'id': 2, 'email': 'bob@example.com'},
    {'id': 3, 'email': 'john@example.com'},
    {'id': 4, 'email': 'bob@example.com'},
    {'id': 5, 'email': 'hulio@example.com'},
    {'id': 6, 'email': 'john@example.com'},
    {'id': 7, 'email': 'john@example.com'}
]

person = pd.DataFrame(person_data)
getAnsw = delete_duplicate_emails(person)
print(getAnsw)


#     person['duplicated'] = person['email'].duplicated(keep='first')
#     person = person[person['duplicated'] == False]
#     person = person.reindex(columns=['id', 'email'])
#     person = pd.DataFrame(person)
#     print(person)