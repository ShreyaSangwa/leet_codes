# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        head=ListNode()
        temp=head
        temp.val=(l1.val+l2.val+carry)%10
        carry=(l1.val+l2.val+carry)//10
        l1=l1.next
        l2=l2.next
        while l1 and l2:
            temp.next=ListNode()
            temp=temp.next
            temp.val=(l1.val+l2.val+carry)%10
            carry=(l1.val+l2.val+carry)//10
            l1=l1.next
            l2=l2.next
        while l1:
            temp.next = ListNode()
            temp=temp.next
            temp.val=(l1.val+carry)%10
            carry=(l1.val+carry)//10
            l1=l1.next
        while l2:
            temp.next = ListNode()
            temp=temp.next
            temp.val=(l2.val+carry)%10
            carry=(l2.val+carry)//10
            l2=l2.next
        if carry:
            temp.next = ListNode()
            temp=temp.next
            temp.val=carry
        return head