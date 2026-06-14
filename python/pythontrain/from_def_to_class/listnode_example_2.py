# https://statisticsglobe.com/list-node-python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode("I")
node2 = ListNode("love")
node3 = ListNode("eat")
node4 = ListNode("shawarma")

node1.next = node2
node2.next = node3
node3.next = node4

# traverse the linked list and print each node's value
current_node = node1
while current_node is not None:
    print(current_node.val)
    current_node = current_node.next