def find_expensive_items(prices_string):
    arr_price=prices_string.split(",")
    print(arr_price)
    sum_num = 0
    middle_num = 0
    arr_hight = []
    str_result = ''
    for x in arr_price:
        sum_num += int(x)
    print(f"sum_num: {sum_num}")
    print(f"len(arr_price): {len(arr_price)}")

    middle_num = sum_num/len(arr_price)
    print(f"middle_num: {middle_num}")
    for x in arr_price:
        if int(x) > middle_num:
            arr_hight.append(x)
    for x in arr_hight:
        str_result += f"{x}\n"
    
    return str_result

# prices_string = input()
prices_string="10,20,30,40,50"
result = find_expensive_items(prices_string)
print(result)