# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = 0
        slow = 0
        mid = head
        while head != None:
            fast+=1
            while slow < (fast//2):
                mid = mid.next
                slow +=1
            head = head.next
        return mid
