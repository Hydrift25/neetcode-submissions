# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        top = root
        if not top:
            return
        curr = top.left
        if curr:
            curr = self.invertTree(curr)
        curr = top.right
        if curr:
            curr = self.invertTree(curr)
        top.left, top.right = top.right, top.left
        return top