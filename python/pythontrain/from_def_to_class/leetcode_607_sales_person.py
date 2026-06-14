import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # print(sales_person)
    # print(company)
    # result = 
    result = pd.merge(sales_person, orders, on="sales_id", how="outer")
    result = pd.merge(result, company, on="com_id", how="outer", suffixes=('', '_com'))
    id_red = result[result["name_com"] == "RED"].reindex(columns=["sales_id"])
    # id_red = pd.merge(id_red, sales_person, on="sales_id", how="left", suffixes=('sales_id_red', '')) #.reindex(columns=[])
    sales_person = sales_person.merge(id_red, on='sales_id', how='left', indicator=True)
    sales_person = sales_person[sales_person["_merge"] == "left_only"].reindex(columns=["name"])

    return(sales_person)




sales_person_data = {
    "sales_id": [1, 2, 3, 4, 5],
    "name": ["John", "Amy", "Mark", "Pam", "Alex"],
    "salary": [100000, 223423, 12123, 500, 123123],
    "commission_rate": [6, 15, 25, 10, 5],
    "hire_date": [2004, 2005, 2012, 999, 2001]
}

company_data = {
    "com_id": [ 1, 2, 3, 4 ], 
    "name": [ "RED", "ORANGE", "YELLOW", "GREEN" ],
    "city": ["Boston", "New York", "Boston", "Austin"]
}

order_id_data = {
    "order_id": [1, 2, 3, 4],
    "order_date": ["2/1/2014", "3/1/2014", "4/1/2014",  "4/1/2012"],
    "com_id": [3, 4, 1, 1],
    "sales_id": [4, 5, 1, 4],
    "amount": [10000, 5000, 50000, 25000]
}

sales_person_1 = pd.DataFrame(sales_person_data)
company = pd.DataFrame(company_data)
order_id = pd.DataFrame(order_id_data)

get_answ = sales_person(sales_person_1, company, order_id)
print(get_answ)