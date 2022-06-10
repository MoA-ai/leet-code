# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        fake_fake_node = ListNode(-101)

        fake_node = fake_fake_node

        while list1 and list2:
            if list1.val < list2.val:
                fake_node.next = list1
                list1 = list1.next
            else:
                fake_node.next = list2
                list2 = list2.next
            fake_node = fake_node.next

        if list1:
            fake_node.next = list1

        if list2:
            fake_node.next = list2

        return fake_fake_node.next