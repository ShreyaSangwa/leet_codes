# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root,a):
            if not root:
                return
            a.append(root.val)
            preorder(root.left,a)
            preorder(root.right,a)
        
        a=[]
        preorder(root,a)
        return a