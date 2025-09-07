# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1 or not head or not head.next:
            return head
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        b=[]
        for i in range(0,len(a),k):
            c=a[i:i+k]
            for j in c:
                b.insert(i,j)
        print(i)
        if i<len(a)-1 and i!=len(a)-k:
            for j in range(len(a)-i):
                b.pop()
            c=a[i:len(a)]
            for i in c:
                b.append(i)
        head=ListNode()
        temp=head
        for i in b:
            temp.next=ListNode()
            temp=temp.next
            temp.val=i
        return head.next