class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
class List:
    def mergeTwoList(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''Merge two sorted Linked lists'''
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # any of the list has remained to be merged
        tail.next = l1 if l1 else l2
        
        return dummy.next

l = List()

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

mergedList = l.mergeTwoList(l1, l2)

while mergedList:
    print(mergedList.val, end="->")
    mergedList = mergedList.next

        
        