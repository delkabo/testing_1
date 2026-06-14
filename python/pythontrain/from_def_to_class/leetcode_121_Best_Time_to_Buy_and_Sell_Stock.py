from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Ввести проверку что есть большее чем последующее (необяз)
        # для каждого числа высчитывать разницу если оно больше
        # Сравнить каждую пару и выбрать большую
        # Напечатать цену покупки и продажи
        self.prices = prices
        list_diff = []
        z_cnt = 0
        
        for x in self.prices:
            copy_pri = self.prices[z_cnt + 1:]
            for cp_pr in copy_pri:
                if x < cp_pr:
                    print(f"{cp_pr} - {x}")
                    print(cp_pr - x)
                    diff_num = cp_pr - x
                    list_diff += [diff_num]
            if z_cnt == (len(self.prices) - 1):
                break
            z_cnt += 1
            print(list_diff)
        print("---------------")
        if len(list_diff) == 0:
            return 0
        for index, name in enumerate(list_diff):
            # print(index)
            if index < len(list_diff) - 1:
                print(f"{list_diff[index]}  {list_diff[index + 1]}")

                if list_diff[index] > list_diff[index + 1]:
                    mem = list_diff[index + 1]
                    list_diff[index + 1] = list_diff[index]
                    list_diff[index] = mem

        return list_diff[len(list_diff) - 1]


prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
getAnsw = Solution()
print(getAnsw.maxProfit(prices))