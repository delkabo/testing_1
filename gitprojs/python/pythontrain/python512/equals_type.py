objects = [1, 2, 0, 3, 4, 1, True, True, False, [True], None, [None, 1, True], {None}, {1: None}, [False, 1], {345}, {345}, 1, [2], 1, [2], 3, bin(1), bin(3), '0b1', '0b11', 0b11, 0b1]
print(len(objects))


# Правильный 
print(len({id(i) for i in objects}))



# print(x)
# 21 правильный