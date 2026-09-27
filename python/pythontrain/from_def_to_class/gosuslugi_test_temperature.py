def process(input_string: str) -> str:
    arr_input_string = input_string.split()
    print(arr_input_string)
    arr_min = 0
    arr_nul = 0
    arr_plus = 0
    for x in arr_input_string:
        if int(x) < 0:
            arr_min += 1
        elif int(x) == 0:
            arr_nul += 1
        else:
            arr_plus += 1

    return f"Выше нуля: {arr_plus}, ниже нуля: {arr_min}, равна нулю: {arr_nul}"
# input_string = input()
input_string="5 -2 0 0 7 8 -1"
output_string = process(input_string)
print(output_string)

# Входные данные: 5 -2 0 0 7 8 -1
# Выше нуля: 3, ниже нуля: 2, равна нулю: 2