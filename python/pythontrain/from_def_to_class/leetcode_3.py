class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        self.s = s
        a_num = 0
        b_num = 0
        arr = []
        arr_str = []
        join_str = ""
        num = 0
        for x in self.s:
            num += 1
            a_num = b_num
            b_num = x
            print(f"a_num: {a_num}; b_num: {b_num}")
            if a_num != b_num:
                if len(arr_str) > 0:
                    if arr_str[len(arr_str)-1] != join_str:
                        # num += 1
                        join_str = join_str + b_num
                elif len(join_str) > 1 and b_num == join_str[0]:
                    print("!!!!!")
                    arr_str.append(join_str)
                    print(f"arr_str: {arr_str}")
                    join_str = ""
                else:
                    # num += 1
                    print(f"join_str start: {join_str}")
                    join_str = join_str + b_num # Вопросики
                    print(f"join_str end: {join_str}")
                    print()
            # elif a_num == b_num or b_num == join_str[0] and len(join_str) > 1:
            elif len(join_str) > 1 and b_num != join_str[0]:
                join_str = join_str + b_num
            else:

                # if join_str is not None:
                #     if b_num == join_str[0]:
                #         print(f"b_num: {b_num}, join_str[0]: {join_str[0]}")
                arr_str.append(join_str)
                print(f"arr_str: {arr_str}")
                join_str = ""
                # arr.append(num)
                # num = 0
            print(f"arr: {arr}; arr_str: {arr_str}")
            print(f"join_str: {join_str}")
            print(f"num: {num}")

        print(f"arr: {arr}; arr_str: {arr_str}")
        # sorted_arr = sorted(arr, reverse=True)
        # return(sorted_arr[0])

mass_input = ["abcabcbb",  "bbbbb", "pwwkew"]
get_answ = Solution()
# for x in mass_input:
#     print(f"{x}: {get_answ.lengthOfLongestSubstring(mass_input)}")
# print()
print(get_answ.lengthOfLongestSubstring(mass_input[0]))