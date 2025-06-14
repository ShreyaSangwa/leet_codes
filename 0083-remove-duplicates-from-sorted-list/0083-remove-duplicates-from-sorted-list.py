# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        if not head:
            return None
        if head.next == None:
            return head
        while head:
            a.append(head.val)
            head=head.next
        a=list(set(a))
        a.sort()
        if len(a)==1:
            root=ListNode()
            root.val=a[0]
            return root
        root=ListNode()
        temp=root
        for i in range(len(a)-1):
            temp.val=a[i]
            temp.next=ListNode()
            temp=temp.next
        temp.val=a[i+1]
        return root
        