"""
Задача 3: Длина слов
Темы: Строки, Циклы, Условия

На вход подается строка, содержащая слова, разделенные пробелами. Определите, сколько слов имеют длину больше 5 символов.

Формат ввода: Одна строка, содержащая слова из латинских букв, разделенные пробелами. Длина строки не превышает 200 символов.

Формат вывода: Одно целое число — количество слов длиннее 5 символов.

Пример 1:
Входные данные: apple banana cherry date
Выходные данные: 2

Пример 2:
Входные данные: cat dog bird
Выходные данные: 0
"""

def string_more_five(var_string: str) -> str:
    var_string_split = var_string.split()
    count_str = 0
    for x in var_string_split:
        if len(x) > 5:
            count_str += 1

    return count_str

# var_str = input()
var_str = "cat dog bird"
get_answ = string_more_five(var_str)
print(get_answ)