# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def post(root,a):
            if not root:
                return
            post(root.left,a)
            post(root.right,a)
            a.append(root.val)
        a=[]
        post(root,a)
        return a