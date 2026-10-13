# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = deque()
        p = head
        while p:
            first.append(p.val)
            p = p.next
        
        
        h = head 
        while h and first:
            print(f"Before: {first = }")
            h.val = first.popleft()
            h = h.next 
            if first:
                h.val = first.pop()
                h = h.next
        
    
