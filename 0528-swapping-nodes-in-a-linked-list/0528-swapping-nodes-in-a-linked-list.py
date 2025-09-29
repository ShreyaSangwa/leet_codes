# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        len=0
        temp=head
        while temp:
            len+=1
            temp=temp.next
        len=len-k+1
        print(len,k)
        temp=head
        if len<=k:
            while len-1:
                temp=temp.next
                len-=1
                k-=1
            a=temp
            while k-1:
                temp=temp.next
                k-=1
            c=a.val
            a.val=temp.val
            temp.val=c
            return head
        else:
            while k-1:
                temp=temp.next
                len-=1
                k-=1
            a=temp
            while len-1:
                a=a.next
                len-=1
            c=a.val
            a.val=temp.val
            temp.val=c
            return head