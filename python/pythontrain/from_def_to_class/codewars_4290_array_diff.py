def array_diff(a, b):
    new_list = []
    count_a = 1
    for x in a:
        print(f"Шаг: {count_a}")
        count_b=0
        for z in b:
            count_b += 1
            if x == z:
                break
            else:
                if count_b == len(b) and x != z:
                    print(f"{x} != {z}")
                    new_list += [x]
                    print(new_list)
            # if len(b) == count:
            #     break
        count_a += 1
    return new_list




a = [1, 2, 2, 2, 3, 5, 4, 20, 11]
b = [1, 2, 20]
print(array_diff(a, b))