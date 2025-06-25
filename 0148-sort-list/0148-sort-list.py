# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        a.sort()
        b=ListNode(val=a[0])
        temp=b
        for i in range(1,len(a)):
            temp.next=ListNode()
            temp=temp.next
            temp.val=a[i]
        return b