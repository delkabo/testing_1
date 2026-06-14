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
            if len(join_str) > 0 and b_num != join_str[0] or a_num != b_num:
                if join_str != "":
                    if len(join_str) > 0 and b_num in join_str:
                        print("OOOOOOOOOOOOOOo")
                        arr_str.append(join_str)
                        print(f"arr_str: {arr_str}")
                        join_str = ""
                print(f"if ---------1")
                join_str = join_str + b_num
            if len(self.s) == num:
                arr_str.append(join_str)

            print(f"arr: {arr}; arr_str: {arr_str}")
            print(f"join_str--: {join_str}")
            print(f"num: {num} +++++++++++++++++++++++++++ END")

        print(f"arr: {arr}; arr_str: {arr_str}")
        sorted_arr = sorted(arr_str, key=len, reverse=True)
        return(len(sorted_arr[0]))

mass_input = ["abcabcbb",  "bbbbb", "pwwkew"]
get_answ = Solution()
# for x in mass_input:
#     print(f"{x}: {get_answ.lengthOfLongestSubstring(mass_input)}")
# print()
print(get_answ.lengthOfLongestSubstring(mass_input[2]))