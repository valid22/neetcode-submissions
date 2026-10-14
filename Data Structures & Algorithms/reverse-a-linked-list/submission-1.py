# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
            
        p = head 
        np = ListNode(p.val)

        while p.next:
            p = p.next
            np = ListNode(p.val, np)

        return np