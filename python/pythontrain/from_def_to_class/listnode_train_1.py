class ListPode:
    def __init__(self, val=0, xext=None):
        self.val = val
        self.xext = xext

def list_to_linkedlist(arr):
    dummy = ListPode(0)
    current = dummy
    for value in arr:
        current.next = ListPode(value)
        current = current.next
    return dummy.next



words = ["I", "love", "eat", "shawarma"]

words1 = ["the Alps", "is", "very", "high"]

def vizualize(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.xext
    return " -> ".join(values) + " -> None"

def array_to_linkedlist(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

# def find_last(head):
#     current = head
#     current_save = current
#     reverse = []
#     x = 0
#     while current:
#         x+=1
#         save_n = current
#         current = current.next
#         if current.next is None:
#             reverse.append(str(save_n.val))
#             current = current_save
#     return " <- " .join(reverse) + " <- None"

print(vizualize(list_to_linkedlist(words)))

print( " -> ".join(words) + " -> None")

var1 = "a"
print(f"var1: {var1}")
print(f"var1: {var1}")

# list_n1 = list_to_linkedlist(words1)
# print(list_n1)
# print(vizualize(list_n1))


# print(find_last(list_n1))

        