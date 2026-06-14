# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

# class Solution:
#     def addTwoNumbers(self, l1: list[int], l2: list[int]) -> list[int]:
#         self.l1 = l1
#         self.l2 = l2
#         # print(l1)
#         reverse_l1 = self.reverse_func(self.l1)
#         reverse_l2 = self.reverse_func(self.l2)
#         # reverse_l1 = int(str(reverse_l1))
#         reverse_l1 = self.transform_int(reverse_l1)
#         reverse_l2 = self.transform_int(reverse_l2)

#         sum_numb = reverse_l1 + reverse_l2

#         list_sum_numb = str(sum_numb)
#         list_sum_numb = list(list_sum_numb)
#         list_sum_numb = self.reverse_func(list_sum_numb)
#         # print(f"list_sum_numb: {list_sum_numb}")

#     def transform_int(self, chislo):
#         # print("transform_int")
#         num = 0
#         for d in chislo:
#             num = num * 10 + d
#         return num


#     def reverse_func(self, list_get):
#         list2 = []
#         # print(f"Последняя {len(list_get)-1}")
#         for count_x in range(len(list_get)-1, -1, -1):
#             print(list_get[count_x])
#             list2.append(list_get[count_x])

#         return list2

# l1 = [2,4,3]
# l2 = [5,6,4]
# getAnsw = Solution()
# print(getAnsw.addTwoNumbers(l1, l2))
# print(getAnsw.reverse_func())


##########################################################
# Definition for singly-linked list.




# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         prev: Optional[ListNode] = None
#         current: Optional[ListNode] = l1


#         # print(l1)

#         # print(f"list_sum_numb: {list_sum_numb}")


#         return list2





# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

words = ["I", "love", "eat", "shawarma"]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        self.l1 = l1
        self.l2 = l2

        list_t_arr_1 = self.listnode_to_array(self.l1)
        list_t_arr_2 = self.listnode_to_array(self.l2)

        reverse_l1 = self.reverse_func(list_t_arr_1)
        reverse_l2 = self.reverse_func(list_t_arr_2)
        # reverse_l1 = int(str(reverse_l1))
        reverse_l1 = self.transform_int(reverse_l1)
        reverse_l2 = self.transform_int(reverse_l2)

        sum_numb = reverse_l1 + reverse_l2

        list_sum_numb = str(sum_numb)
        list_sum_numb = list(list_sum_numb)
        list_sum_numb = self.reverse_func(list_sum_numb)

        answ_var = self.list_to_linkedlist(list_sum_numb)
        print(type(answ_var))
        return answ_var
    # print(f"list_sum_numb: {list_sum_numb}")

    def listnode_to_array(self, head):
        arr_1 = []
        current = head
        while current:
            arr_1.append(int(current.val))
            current = current.next
        return arr_1

    def transform_int(self, chislo):
        # print("transform_int")
        num = 0
        for d in chislo:
            num = num * 10 + int(d)
        return num


    def reverse_func(self, list_get):
        list2 = []
        # print(f"Последняя {len(list_get)-1}")
        for count_x in range(len(list_get)-1, -1, -1):
            print(list_get[count_x])
            list2.append(list_get[int(count_x)])

        return list2

    def list_to_linkedlist(self, arr):
        dummy = ListNode(0)
        current = dummy
        for val in arr:
            current.next = ListNode(int(val))
            current = current.next
        return dummy.next

l1 = list_to_linkedlist([2,4,3])  # стало ListNode
l2 = list_to_linkedlist([5,6,4])  # стало ListNode


