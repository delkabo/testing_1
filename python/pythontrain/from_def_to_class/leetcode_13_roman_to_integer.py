class Solution:
    def romanToInt(self, s: str) -> int:
        s_num = str(s)
        s_num = s_num[::-1]
        # print(s_num)
        rom_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000 
        }
        n_end = []
        n_mem = 0
        start = 0
        result = 0
        for x in s_num:
            print(f"x: {start}")
            if start == 0:
                n_mem = rom_num[x]
            # n_mem = rom_num[x]
            if n_mem > rom_num[x]:
                n_mem -= rom_num[x]
            else:
                if start != 0:
                    n_end.append(n_mem)
                n_mem = rom_num[x]
            start +=1
            if start == len(s_num):
                n_end.append(rom_num[x])
        
        
        for x in n_end:
            print(x)
            result += x
        return result

s = "MCMXCIV"
getAnsw = Solution()
print(getAnsw.romanToInt(s))