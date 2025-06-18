# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rotate(head):
            temp=head
            while temp.next.next!=None:
                temp=temp.next
            a=temp.next
            temp.next=None
            a.next=head
            head=a
            return head
        if not head:
            return head
        if not head.next:
            return head
        temp=head
        length=0
        while temp:
            temp=temp.next
            length+=1
        while length<k:
            k=k-length
        for i in range(k):
            head=rotate(head)
        return head