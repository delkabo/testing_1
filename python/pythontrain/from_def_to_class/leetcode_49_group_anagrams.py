import time
time_await = 0
class Solution(object):
    def groupAnagrams(self, strs):
        # :type strs: List[str]
        # :rtype: List[List[str]]
        self.strs = strs
        copy_strs = self.strs[:]
        list_main = []
        list_time = []
        count_x = 1
        # for x in range(0, len(copy_strs)):
        x = 0
        if len(copy_strs) == 0:
            list_main = [[]]
            return list_main
        else:
            while x < len(copy_strs): 
                print(f"x ---- {x}")
                print(f"Длина copy_strs: {len(copy_strs)}: {copy_strs}")
                if len(copy_strs) != 0:
                    print(f"Элемент: {count_x}; x = {copy_strs[x]}")
                    list_time.append(copy_strs[x])
                    # for z in range(0, len(copy_strs)):
                    z = 0
                    while z != len(copy_strs) - 1: 
                        time.sleep(time_await)
                        print(f"x: {copy_strs[x]}; z_mass: {copy_strs[z]}; z: {z}")
                        if sorted(copy_strs[x]) == sorted(copy_strs[z]):
                            if copy_strs[z] != copy_strs[x]:# and not self.searchElem(z, list_main):
                                list_time.append(copy_strs[z])
                                copy_strs.pop(z)
                                z = 0
                                print(f"list_time: {list_time}")
                        z += 1
                        time.sleep(time_await)
                        # Если последний элемент, то обнуляем временный массив
                        # if z == len(self.strs) - 1:
                    time.sleep(time_await)
                    if len(list_time) != 0:
                        list_main.append(list_time)
                    list_time = []
                    print(f"ДО: {copy_strs}")
                    # copy_strs.pop(x)
                    print(f"ПОСЛЕ: {copy_strs}")
                    print(list_main)
                            # И проверять каждый раз в других массивах

                        # Написать функцию, которая ищет во вложенных списках
                count_x += 1
                x += 1
            return list_main
    def searchElem(self, elem, mass):
        for x in mass:
            if isinstance(x, list):
                searchElem(elem, x)
            else:
                if elem == x:
                    return True

strs = ["eat","tea","tan","ate","nat","bat"]
strs = []
getAnsw = Solution()
print(getAnsw.groupAnagrams(strs))
