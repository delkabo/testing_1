import pandas as pd

class GetResult():
    def __init__(self, product: pd.DataFrame, sales: pd.DataFrame):
        self.product = product
        self.sales = sales
        self.merged_table = None
        self.merged_table_drop = None

    def print_merged_table(self):
        print(self.merged_table)

    def print_merged_table_drop(self):
        print(self.merged_table_drop)

    def merge_table(self):
        self.merged_table = pd.merge(self.sales, self.product, on="product_id", how="left")
        return self

    def copy_table(self):
        self.merged_table_drop = self.merged_table.copy(deep=True)
        return self

    def merge_sort(self):
        self.merged_table = self.merged_table[self.merged_table["sale_date"] <= '2019-03-31']
        return self

    def sort_drop(self):
        self.merged_table_drop = self.merged_table_drop[self.merged_table_drop["sale_date"] > '2019-03-31'].reindex(columns=["product_id"])
        return self

    def merge_1(self):
        self.merged_table = self.merged_table.merge(self.merged_table_drop, on="product_id", how="left", indicator=True)
        # print(self.merged_table)
        # print(self.merged_table_drop)
        return self

    def merge_2(self):
        self.merged_table = self.merged_table[self.merged_table["_merge"] == "left_only"].reindex(columns=["product_id", "product_name"])
        # print(self.merged_table)
        return self

    def get_answer(self) -> pd.DataFrame:
        return self.merged_table
    
    # def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    #     print()
    #     #merged_table = pd.merge(sales, product, on="product_id", how="left")
    #     #merged_table_drop = merged_table.copy(deep=True)
    #     #merged_table = merged_table[merged_table["sale_date"] <= '2019-03-31']
    #     #merged_table_drop = merged_table_drop[merged_table_drop["sale_date"] > '2019-03-31'].reindex(columns=["product_id"])
    #     #merged_table = merged_table.merge(merged_table_drop, on="product_id", how="left", indicator=True)
    #     #merged_table = merged_table[merged_table["_merge"] == "left_only"].reindex(columns=["product_id", "product_name"])
    #     return merged_table


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

get_answ = GetResult(product, sales)
print(get_answ.merge_table().copy_table().merge_sort().sort_drop().merge_1().merge_2().get_answer())