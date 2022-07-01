# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(t1, t2, parent=None, dir=None) -> TreeNode:
            if t1 == None and t2 == None:
                return

            # visit
            v1 = t1.val if t1 != None else 0
            v2 = t2.val if t2 != None else 0
            t3 = TreeNode(v1+v2)

            if parent != None:
                if dir == 'l':
                    parent.left = t3
                elif dir == 'r':
                    parent.right = t3

            # left
            dfs(t1.left if t1 !=None else None, t2.left if t2 != None else None, t3, 'l')

            # right
            dfs(t1.right if t1 != None else None, t2.right if t2 != None else None, t3, 'r')

            return t3

        return dfs(root1, root2)