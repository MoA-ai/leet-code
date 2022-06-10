# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None

        nodes = []

        nodes.append(head)
        while nodes[-1].next != None:
            nodes.append(nodes[-1].next)

        target = nodes[-n]
        target_before = nodes[-n-1] if -n-1 >= 0 else None
        target_next = nodes[-n].next if nodes[-n].next != None else None
        target_before.next = target_next if target_before != None else None

        return head