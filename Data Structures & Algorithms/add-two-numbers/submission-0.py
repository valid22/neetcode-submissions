# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sh = su = ListNode()
        
        a = l1
        b = l2 
        r = 0
        while a or b or r:
            s = (a.val if a else 0) + (b.val if b else 0) + r
            if s > 9:
                r = 1
                s = s % 10
            else:
                r = 0
            
            a = a and a.next 
            b = b and b.next 
            
            su.next = ListNode(s)
            su = su.next
        
        return sh.next