import pandas as pd

class CustomersSearch():
    def __init__(self, customers: pd.DataFrame, orders: pd.DataFrame):
        self.customers = customers
        self.orders = orders
        self.result = None
        self.result_filter = None

    def print_table(self): # -> pd.DataFrame:
        print(f"customers:\n{self.customers}")
        print(f"orders:\n{self.orders}")
        print(f"result:\n{self.result}")
        print(f"result_filter:\n{self.result_filter}")

    def st_1_merge(self):
        self.result = pd.merge(self.customers, self.orders, left_on='id', right_on='customerId', how='outer')
        print(self.result)
        return self

    def st_2_isna(self):
        self.result_filter = self.result[self.result['customerId'].isna()]
        print(self.result_filter)
        return self

    def st_3_reindex(self):
        self.result_filter = self.result_filter.reindex(columns=['name'])
        print(self.result_filter)
        return self

    def st_4_rename(self):
        self.result_filter = self.result_filter.rename(columns={'name': 'Customers'})
        print(self.result_filter)
        return self

    # @property
    def return_result(self) -> pd.DataFrame:
        return self.result_filter



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
# getAnsw = find_customer(customers, orders)
# print(getAnsw)

getAnswClass = CustomersSearch(customers, orders)
getAnswClass.print_table()
getAnswClass.st_1_merge().st_2_isna().st_3_reindex().st_4_rename().return_result()
