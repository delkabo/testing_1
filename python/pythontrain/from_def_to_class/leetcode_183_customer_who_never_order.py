import pandas as pd

def find_customer(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(customers, orders, left_on='id', right_on='customerId', how='outer')
    result_filter = result[result['customerId'].isna()]
    result_filter = result_filter.reindex(columns=['name'])
    result_filter = result_filter.rename(columns={'name': 'Customers'})
    return result_filter

customers_data = [
    {'id': 1, 'name': 'Joe'},
    {'id': 2, 'name': 'Henry'},
    {'id': 3, 'name': 'Sam'},
    {'id': 4, 'name': 'Max'},
]

orders_data = [
    {'id': 1, 'customerId': 3},
    {'id': 2, 'customerId': 1}
]

orders = pd.DataFrame(orders_data)
customers = pd.DataFrame(customers_data)
getAnsw = find_customer(customers, orders)
print(getAnsw)