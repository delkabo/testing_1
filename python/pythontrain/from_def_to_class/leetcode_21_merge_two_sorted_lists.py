# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        self.node_list1 = list1
        self.node_list2 = list2
        # list1 = self.listnode_to_list(self.node_list1)
        # list2 = self.listnode_to_list(self.node_list2)
        newlist = self.node_list1 + self.node_list2
        newlist.sort()
        print(newlist)
        # return newlist
        result_listnode = self.list_to_listnode(newlist)
        return self.listnode_to_list(result_listnode)
    def list_to_listnode(self, get_list):
        dummy = ListNode(0)
        current = dummy
        for x in get_list:
            print(f"-- {x}")
            current.next = ListNode(x)
            current = current.next
        return dummy.next
    def listnode_to_list(self, get_list):
        new_array = []
        current = get_list
        while current is not None:
            print(current.val)
            new_array.append(current.val)
            current = current.next
        
        return new_array
list1 = [1,2,4]
list2 = [1,3,4]
get_answ = Solution()
answer1 = get_answ.mergeTwoLists(list1, list2)
print(answer1)
            