# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def idk(tree, a):
            if tree is None:
                a.append(None)
                return
            a.append(tree.val)
            idk(tree.left,a)
            idk(tree.right,a)
        
        a=[]
        b=[]
        idk(p,a)
        idk(q,b)
        return a==b