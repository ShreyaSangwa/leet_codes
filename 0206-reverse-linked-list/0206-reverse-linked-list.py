# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        a=ListNode(val=head.val)
        head=head.next
        while head:
            temp=ListNode(val=head.val)
            temp.next=a
            a=temp
            head=head.next
        return a