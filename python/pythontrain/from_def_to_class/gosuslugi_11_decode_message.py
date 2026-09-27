"""
Задача 11: Расшифровка сообщения
Темы: Строки, Циклы, Условия, Срезы

Вам пришло зашифрованное сообщение. Шифр простой: каждый символ сдвинут на 3 позиции вперед по алфавиту (регистр сохраняется). Например, 'a' → 'd', 'x' → 'a', 'Z' → 'C'. Пробелы и знаки препинания остаются без изменений. Расшифруйте сообщение.

Формат ввода: Одна строка с зашифрованным сообщением (только латиница, пробелы и базовые знаки препинания).

Формат вывода: Расшифрованная строка.

Пример 1:
Входные данные: "Krzg, zruog!"
Выходные данные: "How, world!"

Пример 2:
Входные данные: "Wkhvh duh qrw wkh gurgv"
Выходные данные: "These are not the droids"
"""

def DecodeMessage(strs):
    upper_letter = 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z'
    arr_upper = upper_letter.split(", ")
    lower_letter = 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'
    arr_lower = lower_letter.split(", ")
    arr_strs = strs.split()
    print(arr_strs)
    new_word = ''
    new_word_str = ''
    leter_get = ''
    get_x = 0
    for letter in strs:
        if letter.isalpha():
            if letter.islower():
                for x in range(0, len(arr_lower)):
                    if letter == arr_lower[x]:
                        get_x = x
                        if get_x-3 < 0:
                            get_x = len(arr_lower) - (0 - get_x)
                            leter_get = arr_lower[get_x]
                        else:
                            leter_get = str(arr_lower[get_x-3])
                        new_word += leter_get
            elif letter.isupper():
                for x in range(0, len(arr_upper)):
                    if letter == arr_upper[x]:
                        get_x = x
                        if get_x-3 < 0:
                            get_x = len(arr_upper) - (0 - get_x)
                            leter_get += arr_upper[get_x]
                        else:
                            leter_get = arr_upper[get_x-3]
                        new_word += leter_get
        else:
            new_word+=letter
    # for x in new_word:
    #     new_word_str +=
    print(new_word)

strs = "Wkhvh duh qrw wkh gurlgv"
DecodeMessage(strs)
