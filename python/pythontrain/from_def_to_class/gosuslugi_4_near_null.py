def near_null(list_num: str) -> int:
    split_ln = list_num.split(", ")
    print(split_ln)
    plus_arr = []
    minus_arr = []
    for x in range(0, len(split_ln)):
        int_ln = int(split_ln[x])
        if int_ln > 0:
            plus_arr.append(int_ln)
        elif int_ln < 0:
            minus_arr.append(int_ln)
    b = 0

    for x in range(1, len(plus_arr)):
        int_1 = int(plus_arr[x-1])
        int_2 = int(plus_arr[x])
        if int_1 > int_2:
            b = plus_arr[x-1]
            plus_arr[x-1] = plus_arr[x]
            plus_arr[x] = b 
        print(plus_arr)

    for x in range(1, len(minus_arr)):
        int_1 = int(minus_arr[x-1])
        int_2 = int(minus_arr[x])
        if int_1 < int_2:
            b = minus_arr[x-1]
            minus_arr[x-1] = minus_arr[x]
            minus_arr[x] = b 
        print(minus_arr)

        if int(minus_arr[0]) * -1 == int(plus_arr[0]):
            return plus_arr[0]
        elif int(minus_arr[0]) * -1 < int(plus_arr[0]):
            return minus_arr[0]


nums1 = '-5, -2, 3, 4, 1'
nums2 = '-3, -2, 2, 3'

getAnsw1 = near_null(nums1)
print(getAnsw1)
getAnsw2 = near_null(nums2)
print(getAnsw2)