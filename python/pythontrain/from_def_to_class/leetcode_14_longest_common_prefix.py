class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # arr_str = strs.split(",")
        arr_pref = ''
        # print(strs[0])
        for count_let in range(0, len(strs[0])):
            for c_word in range(0, len(strs)):
                if len(strs[c_word]) < count_let + 1:
                    print("Тутта")
                    break
                # print(strs[c_word])
                print(f"ЭТАЛОННАЯ БУКВА: {strs[0][count_let]}")
                print(f"Полученная буква: {strs[c_word][count_let]}")
                print(f"c_word {c_word}")

                if strs[c_word][count_let] != strs[0][count_let]:
                    break
                elif c_word == len(strs) - 1:
                    print("Я здесь +++++")
                    if strs[c_word][count_let] == strs[0][count_let]:
                        print("Я здесь !!!!!!!!")
                        arr_pref+=str(strs[0][count_let])
                        print(arr_pref)


        if len(arr_pref) < 2:
            return ""
        else:
            return arr_pref


strs = ["flower","flow","flight"]
get_answ = Solution().longestCommonPrefix(strs)
print(f"{get_answ}")