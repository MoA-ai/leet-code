# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q = deque()
        while head != None:
            q.append(head)
            head = head.next

        q.reverse()
        h = ListNode()
        t = h
        for item in q:
            t.next = item
            t = t.next
        t.next = None

        return h.next