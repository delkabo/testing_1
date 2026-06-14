# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        self.head = head
        self.k = k
        get_array = self.listnode_to_arr(self.head)
        
            
    def reverese_arr(main_arr, k):
        temp_arr = []
        temp_arr_rev = [] 
        num_int = len(get_array) // k
        # if num_int == 1:
        print(f"num_int: {num_int}")
        # Проделываем перворот столько раз сколько полных раз у нас получилось значение
        for k_start in num_int:
            # k_start - шаг
            # k - длинна шага
            # Умножаем, чтобы в массиве поэтапно использовались индексы группами
            k_modif = k * k_start
            for k_count in range(k_start-1, k_start):
                for x in range(k_modif-1, k_modif):
                    temp_arr.append(main_arr[x])
                for x in range(len(temp_arr)-1, -1, -1):
                    temp_arr_rev.append(temp_arr[x])
                
                # Приравниваем перевернутый массив
            for x in range(0, len(temp_arr_rev) - 1):
                z = x
                if k_start > 1 and x == 0:
                    z = k_start * k
                    main_arr[x+k_modif-1] = temp_arr_rev[x]# Всегда будет 0 
                # k_start - хута, нужно прибвлять




        # elif num_int > 1:
        #     print()

    def listnode_to_arr(self, head):
        local_arr = []
        current = head
        while current:
            local_arr.append(current.val)
            current = current.next
        return local_arr

    def arr_to_listnode(self, array1):
        dummy = ListNode(0)
        current = dummy.next
        for x in array1:
            current.next = ListNode(x)
            current = current.next
        return dummy.next