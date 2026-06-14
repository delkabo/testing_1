import pandas as pd

# def sales_analysis(product, sales):
#     return pd.merge(product, sales, on='product_id').groupby('category').sum()

# def sales_analysis(product, sales):
#     mem_table = pd.merge(product, sales, on='product_id', how='left')
#     # return mem_table
#     mem_table = mem_table.reindex(columns=['pruduct_id', 'category', 'kilogram'])
#     print(mem_table)
#     return mem_table.groupby('category').sum()



class ClassTable():
    def __init__(self, product, sales):
        self.product = product
        self.sales = sales
        self._merged = None


    def sales_analysis(self):
        mem_table = pd.merge(product, sales, on='product_id', how='left')
        mem_table = mem_table.reindex(columns=['pruduct_id', 'category', 'kilogram'])
        return mem_table.groupby('category').sum()




product = pd.DataFrame({
    'product_id': [1, 2, 3, 4],
    'name' : ['banana', 'orange', 'bread', 'cupcakes'], 
    'category' : ['fruits', 'fruits', 'backery', 'backery']
    # 'category' : [2, 2, 5, 5]
}) 

sales = pd.DataFrame({
    'product_id': [2, 3, 4, 3],
    'kilogram': [100, 22, 3, 45],
    'market' : ['shesterka', 'shesterka', 'shesterka', 'pyaterka']
}) 

getAnsw = ClassTable(product, sales)
print(getAnsw.sales_analysis())