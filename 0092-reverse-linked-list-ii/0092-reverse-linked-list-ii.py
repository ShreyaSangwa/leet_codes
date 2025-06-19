# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        a=ListNode()
        temp=a
        right-=left-1
        while head and left>1:
            temp.next=ListNode(val=head.val)
            temp=temp.next
            head=head.next
            left-=1
        b=[]
        while head and right>0:
            b.append(head.val)
            head=head.next
            right-=1
        b=b[::-1]
        for i in b:
            temp.next=ListNode(val=i)
            temp=temp.next
        while head:
            temp.next=ListNode(val=head.val)
            temp=temp.next
            head=head.next
        return a.next