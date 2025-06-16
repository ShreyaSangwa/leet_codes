# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=ListNode()
        temp=a
        if not head or not head.next:
            return head
        if head and head.next:
            temp.val=head.next.val
            temp.next=ListNode()
            temp=temp.next
            temp.val=head.val
            if head.next.next:
                head=head.next.next
            else:
                return a
        while head and head.next:
            temp.next=ListNode()
            temp=temp.next
            temp.val=head.next.val
            temp.next=ListNode()
            temp=temp.next
            temp.val=head.val
            if head.next.next:
                print(1)
                head=head.next.next
            else:
                break
        if head and not head.next:
            temp.next=ListNode(val=head.val)
        return a