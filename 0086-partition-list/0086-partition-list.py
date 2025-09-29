# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        a=[]
        while(head):
            a.append(head.val)
            head=head.next
        before=[]
        same=[]
        for i in a:
            if i<x:
                before.append(i)
            else:
                same.append(i)
        before=before+same
        temp=ListNode()
        head=temp
        for i in before:
            temp.next=ListNode()
            temp=temp.next
            temp.val=i
        return head.next