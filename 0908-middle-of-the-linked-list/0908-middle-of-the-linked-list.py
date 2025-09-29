# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        len=0
        while temp:
            len+=1
            temp=temp.next
        len=len//2
        mid=head
        while len:
            mid=mid.next
            len-=1
        return mid