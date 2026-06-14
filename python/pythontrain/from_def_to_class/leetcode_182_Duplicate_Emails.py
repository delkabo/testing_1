import pandas as pd

def dublicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    print()
    get_dubl = person.duplicated(subset=None, keep='first') #['email'])
    get_dubl_group = person.groupby(['email']).filter(lambda x: len(x) > 1).drop_duplicates(subset='email')
    get_dubl_group = get_dubl_group.rename(columns={'email': 'Email'})
    get_dubl_group = get_dubl_group.reindex(columns=['Email'])
    return get_dubl_group

person_data = [
    {'id': 1, 'email': 'a@b.com'},
    {'id': 2, 'email': 'c@d.com'},
    {'id': 3, 'email': 'a@b.com'},
    {'id': 4, 'email': 'c@d.com'},
    {'id': 5, 'email': 'a@b.com'},
    {'id': 6, 'email': 'c@d.com'},
    {'id': 7, 'email': 'a@b.com'},
    {'id': 8, 'email': 'e@f.com'}
]

person = pd.DataFrame(person_data)
getAnsw = dublicate_emails(person)

print(getAnsw)