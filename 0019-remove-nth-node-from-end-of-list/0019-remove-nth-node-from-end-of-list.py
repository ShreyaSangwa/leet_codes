# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head and not head.next:
            return None
        length=0
        temp=head
        while temp:
            length+=1
            temp=temp.next
        temp=head
        if length==n:
            head=head.next
        elif length==n+1:
            if head.next.next:
                head.next=head.next.next
            else:
                head.next=None
        else:
            while length>n+1:
                temp=temp.next
                length-=1
            temp.next=temp.next.next
        return head