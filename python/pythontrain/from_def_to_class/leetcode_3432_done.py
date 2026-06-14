class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums=nums
        List = []
        List2 = []
        print("Nums: ", self.nums)
        for x_ch in self.nums:
            print(x_ch)
            if self.is_integer_instance(x_ch):
                print("This is int ", x_ch)
                List.append(x_ch)
            else:
                return "Error is not a integer"

                
        
        num_is_even = 0
        len_list = len(List)
        list_copy = List.copy()
        print("++++++++++++++++++", len_list)
        for x in range(1, len_list):
            print("??????????????? x-1: ", x-1)
            add_num = list_copy.pop(0)
            # массив уменьшается и нужно перечитывать
            print("List.pop[x-1] ", add_num)
            List2.append(add_num)
            print("List2: ", List2)
            print("List: ", list_copy)
            l2=0
            for xl2 in List2:
                l2+=xl2
            el=0
            for xl in List:
                el+=xl

            print("!!!!!!!!!!!!!!!!!!!!!", l2,"-",el,")%",2)
            l2=(l2-el)%2
            print("l2:", l2)
            if l2 == 0:
                num_is_even+=1
            
        return num_is_even

    def is_integer_instance(self, numbers):
        return isinstance(numbers, int)

        
        
# input("Enter number")
nums=[10,10,3,7,6]
get_sol=Solution()
result = get_sol.countPartitions(nums)
print("result: ", result)

