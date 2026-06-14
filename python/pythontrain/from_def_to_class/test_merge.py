import pandas as pd

# Таблица с исходными данными
main_df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'value': [100, 200, 300, 400, 500, 600]
})

# Таблица с ID, которые нужно исключить
exclude_df = pd.DataFrame({
    'id': [2, 4, 6],
    'reason': ['duplicate', 'inactive', 'blocked']
})

# Соединяем с индикатором
merged = main_df.merge(exclude_df, on='id', how='left', indicator=True)
print(merged)
# Оставляем только те строки, которые НЕ найдены в exclude_df
result = merged[merged['_merge'] == 'left_only'].drop(columns=['_merge', 'reason'])

print("Результат (исключены ID 2, 4, 6):")
print(result)