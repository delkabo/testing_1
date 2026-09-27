def long_word(words: str) -> str:
    if len(words) > 200:
        return f"Длинна строки не может превышать 200 символов.\nУ вас в строке {len(words)} символов/а"
    split_words = words.split(" ")
    count_words = 0
    arr_words = []
    for x in split_words:
        if len(x) > 5:
            count_words += 1
            arr_words.append(x)

    if count_words > 0:
        return f"Количество слов больше 5 символов равно {count_words}.\nСледующие слова больше пяти: {str(arr_words)}"
    else:
        return "Отсутствуют слова больше 5 символов"

words = 'apple banana cherry date'
getAnsw = long_word(words)
print(getAnsw)