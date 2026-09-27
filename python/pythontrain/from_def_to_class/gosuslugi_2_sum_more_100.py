class more_hundred:
    def __init__(self, list_numbers: str) -> str:
        split_l_n = list_numbers.split(", ")
        sum = 0

    def find_sum(self):
        split_l_n = list_numbers.split(", ")
        print(split_l_n)
        print(len(split_l_n))
        print("+-+-+-+-+-+-+-+-+")
        sum = 0
        for x in range(0, len(split_l_n)):
            get_num = int(split_l_n[x])
            print(f"число: {get_num}, индекс: {x}")
            if get_num > 100:
                sum += get_num
            if x == len(split_l_n) - 1  and sum == 0:
                return f"Нет чисел больше 100"
        return f"Сумма равна {sum}"

# def more_hundred(list_numbers: str) -> str:
#     split_l_n = list_numbers.split(", ")
#     print(split_l_n)
#     print(len(split_l_n))
#     print("+-+-+-+-+-+-+-+-+")
#     sum = 0
#     for x in range(0, len(split_l_n)):
#         get_num = int(split_l_n[x])
#         print(f"число: {get_num}, индекс: {x}")
#         if get_num > 100:
#             sum += get_num
#         if x == len(split_l_n) - 1  and sum == 0:
#             return f"Нет чисел больше 100"
#     return f"Сумма равна {sum}"
        


# list_numbers = '1, 3, 10, 120, 13, 300, 66, 225'
list_numbers = '1, 3, 10, 13, 66'
get_answer = more_hundred(list_numbers)
print(get_answer.find_sum())