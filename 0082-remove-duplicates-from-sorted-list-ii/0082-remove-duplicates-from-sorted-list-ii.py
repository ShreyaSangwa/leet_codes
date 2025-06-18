# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        a={}
        while head:
            if head.val in a:
                a[head.val]+=1
                head=head.next
            else:
                a[head.val]=1
                head=head.next
        b=ListNode()
        temp=b
        for i in a:
            if a[i]>1:
                continue
            else:
                temp.next=ListNode()
                temp=temp.next
                temp.val=i
        return b.next