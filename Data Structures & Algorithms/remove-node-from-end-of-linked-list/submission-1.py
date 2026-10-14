# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        c = head

        while c:
            N += 1
            c = c.next

        n = N - n

        c = head
        p = None
        i = 1

        while i <= n and c.next:
            c, p = c.next, c
            i += 1

        if p is None:
            return head.next

        p.next = c.next

        return head