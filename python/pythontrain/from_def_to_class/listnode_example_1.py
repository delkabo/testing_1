# https://statisticsglobe.com/list-node-python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# instantiate the nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

#link the nodes
node1.next = node2
node2.next = node3
node3.next = node4

current_node = node1
while current_node is not None:
    print(current_node.val)
    current_node = current_node.next