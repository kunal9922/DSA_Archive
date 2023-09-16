class linkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Solution():
    def findMiddelNode(self, head: linkedList):
        hare = tortoise = head

        while hare and hare.next:
            # Two step jumps 
            hare = hare.next.next
            # one step jump
            tortoise = tortoise.next
        
        # Middel Node
        return tortoise
