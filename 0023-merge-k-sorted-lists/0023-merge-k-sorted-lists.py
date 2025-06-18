# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        a=[]
        for i in lists:
            while i is not None:
                a.append(i.val)
                i=i.next
        a.sort()
        if a:
            b=ListNode(val=a[0])
            temp=b
            for i in range(1,len(a)):
                b.next=ListNode()
                b=b.next
                b.val=a[i]
            return temp
        else:
            return None