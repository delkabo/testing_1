import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    print()
    merged_table = pd.merge(sales, product, on="product_id", how="left")
    merged_table_drop = merged_table.copy(deep=True)
    merged_table = merged_table[merged_table["sale_date"] <= '2019-03-31']
    merged_table_drop = merged_table_drop[merged_table_drop["sale_date"] > '2019-03-31'].reindex(columns=["product_id"])
    merged_table = merged_table.merge(merged_table_drop, on="product_id", how="left", indicator=True)
    print(merged_table)
    merged_table = merged_table[merged_table["_merge"] == "left_only"].reindex(columns=["product_id", "product_name"])
    return merged_table


product = pd.DataFrame({
    'product_id': [1, 2, 3],
    'product_name': ['S8', 'G4', 'iPhone'],
    'unit_price': [1000, 800, 1400]
})

sales = pd.DataFrame({
    'seller_id': [1, 1, 2, 3],
    'product_id': [1, 2, 2, 3],
    'buyer_id': [1, 2, 3, 4],
    'sale_date': ['2019-01-21', '2019-02-17', '2019-06-02', '2019-05-13'],
    'quantity': [2, 1, 1, 2],
    'price': [2000, 800, 800, 2800]
})

get_answ = sales_analysis(product, sales)
print(get_answ)