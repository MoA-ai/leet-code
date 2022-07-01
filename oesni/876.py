# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = m = 0
        mid_node = head
        while head.next != None:
            l += 1
            while m < (l / 2):
                m += 1
                mid_node = mid_node.next
            head = head.next

        return mid_node