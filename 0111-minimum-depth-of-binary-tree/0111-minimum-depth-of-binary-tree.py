# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: #if root null
            return 0
        if not (root.left or root.right): #if root leaf node
            return 1
        left=1000000
        right=1000000
        if root.left: #if root does not have left but has right then left is considered to have a very large value which gets disregarded
            left=self.minDepth(root.left)
        if root.right: #if root does not have right but has left then right is considered to have a very large value which gets disregarded
            right=self.minDepth(root.right)
        return min(left,right)+1