# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def search(root,d):
            if not root:
                return
            if root.val in d:
                d[root.val]+=1
            else:
                d[root.val]=1
            search(root.left,d)
            search(root.right,d)
        d={}
        search(root,d)
        maxval=max(d.values())
        a=[]
        for i in d:
            if d[i]==maxval:
                a.append(i)
        return a