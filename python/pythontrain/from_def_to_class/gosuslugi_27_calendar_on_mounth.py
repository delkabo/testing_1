"""
Задача 27: Календарь на месяц
Темы: Даты (без модуля datetime), Циклы, Условия

Даны год и месяц (число от 1 до 12). Выведите календарь на этот месяц в виде таблицы (7 столбцов, неделя начинается с понедельника). Первый день месяца должен быть на нужном месте. Пустые ячейки заполните пробелами.

Формат ввода: Два числа через пробел: год и месяц.

Формат вывода: 6-7 строк с числами (форматирование: 2 позиции на число, разделение пробелом).

Пример 1:
Входные данные: 2024 1
Выходные данные:
1 2 3 4 5 6 7
8 9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
"""
mounts = {
1:	31,
2:	28,
3:	31,
4:	30,
5:	31,
6:	30,
7:	31,
8:	31,
9:	30,
10:	31,
11:	30,
12:	31
}

def date_in_mounth(date_str):
    x_count = 0
    print_date = ''
    arr_date_str = date_str.split(" ")
    if len(arr_date_str) > 2:
        raise ValueError("Необходимо вводить месяц в формате 'Год Месяц' - '2003 10'")
    mounth = mounts[int(arr_date_str[1])]
    for x in range(1, mounth + 1):
        x_count += 1
        date_get = str(x)
        if x_count == 7:
            x_count = 0
            date_get += "\n"
            print_date += date_get
        else:
            print_date += date_get + " "
    print_date = f"-- {arr_date_str[0]} --\n{print_date}"
    return print_date
date_str = "2024 3"
get_answ = date_in_mounth(date_str)
print(get_answ)