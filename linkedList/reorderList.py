class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        slow , fast = head, head.next
        # move fast pointer until the end of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # reverse the second half of the list
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
          
        # merge the two halves
        first, second = head, prev
        while second:
            temp1 , temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


l1 : ListNode = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

s = Solution()
s.reorderList(l1)

while l1:
    print(l1.val)
    l1 = l1.next