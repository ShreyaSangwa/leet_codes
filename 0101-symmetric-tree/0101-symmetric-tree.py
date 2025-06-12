# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def idk(tree,a):
            if tree is None:
                a.append(None)
                return
            a.append(tree.val)
            idk(tree.left,a)
            idk(tree.right,a)
        def kdi(tree,a):
            if tree is None:
                a.append(None)
                return
            a.append(tree.val)
            kdi(tree.right,a)
            kdi(tree.left,a)
        a=[]
        b=[]
        idk(root.left,a)
        kdi(root.right,b)
        return a==b