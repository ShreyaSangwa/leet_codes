# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        temp=head
        while temp and temp.next:
            while temp.next and temp.next.val==val:
                if temp.next.next:
                    temp.next=temp.next.next
                else:
                    temp.next=None
            temp=temp.next
        if head.val==val:
            return head.next
        return head