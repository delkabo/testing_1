"""
Задача 4: Ближайшее к нулю
Темы: Списки, Циклы, Условия, Математические операции

На вход подается список целых чисел, разделенных запятыми. Найдите число, наиболее близкое к нулю. Если таких чисел несколько (например, -2 и 2), выведите то, которое больше (положительное). Если список пустой, выведите «Нет данных».

Формат ввода: Одна строка, содержащая целые числа, разделенные запятыми.

Формат вывода: Одно целое число.

Пример 1:
Входные данные: -5, -2, 3, 4, 1
Выходные данные: 1

Пример 2:
Входные данные: -3, -2, 2, 3
Выходные данные: 2
"""

def close_to_null(var_string: str) -> str:
    var_string_split = var_string.split(',')
    num_minus = 0
    num_plus = 0
    # save_plus = 0
    # save_minus = 0
    z = 0
    for x in var_string_split:
        int_x = int(x)
        print(f"int_x: {int_x}")
        print(f"z:{z}")
        print(f"num_plus: {num_plus}")
        print(f"num_minus: {num_minus}")
        if int_x > 0:
            if z == 0 or num_plus == 0:
                num_plus = int_x
            else:
                if int_x < num_plus:
                    num_plus = x
                    print(f"num_plus: {num_plus}")
        elif int_x < 0 or num_minus == 0:
            if z == 0:
                num_minus = int_x
            else:
                if int_x > num_minus:
                    num_minus = x
        else:
            return x

        z += 1
    print(f"num_plus: {num_plus}, num_minus: {num_minus}")
    num_plus = int(num_plus)
    equal_minus = (int(num_minus) * -1)
    print(f"equal_minus: {equal_minus}")
    if equal_minus == num_plus:
        return num_plus
    elif equal_minus > num_plus:
        return num_plus
    elif equal_minus < num_plus:
        print(f"Мы здесь {(num_minus * -1)}")
        return num_minus
    else:
        return "Проблема"

# var_str = input()
var_str = "-5, -2, 3, 4, 1"
get_answ = close_to_null(var_str)
print(f"Ответ: {get_answ}")