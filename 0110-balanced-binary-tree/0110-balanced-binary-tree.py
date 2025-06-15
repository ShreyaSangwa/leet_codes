# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            return max(height(root.left),height(root.right))+1
        if root == None:
            return True
        balance = height(root.left)-height(root.right)
        if balance>1 or balance<-1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)