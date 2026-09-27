def passing_scores(scores: str) -> str:
    "rjl"
    num_stud_good = 0
    num_stud_bad = 0
    result_str = ''
    arr_scores = scores.split()
    for x in arr_scores:
        if int(x) >= 60:
            num_stud_good += 1
        else:
            num_stud_bad += 1

    return f"Прошли {num_stud_good},не прошли {num_stud_bad}"
        

# scores = input()
scores = "30 40 50 60 70"
result = passing_scores(scores)
print(result)