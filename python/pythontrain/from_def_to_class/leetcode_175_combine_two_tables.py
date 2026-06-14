import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(person, address, on="personId", how="left")
    result_slice = result.reindex(columns = ['firstName', 'lastName', 'city', 'state'])
    return result_slice

persons_data = [
    {"personId": 1, "lastName": "Wang", "firstName": "Allen"},
    {"personId": 2, "lastName": "Inwonderland", "firstName": "ALice"}
]

address_data = [
    {"addressId" : 1, "personId": 2, "city": "New York City", "state": "New York"},
    {"addressId" : 2, "personId": 3, "city": "Bambarbia", "state": "Kerkudu"},
]

persons = pd.DataFrame(persons_data)
address = pd.DataFrame(address_data)
getAnsw = combine_two_tables(persons, address)

print(getAnsw)