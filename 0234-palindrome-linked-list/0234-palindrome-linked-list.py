# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a=head
        length=0
        while a:
            length+=1
            a=a.next
        if length==1:
            return True
        stack=[]
        if length%2==0:
            for i in range(length//2):
                stack.append(head.val)
                head=head.next
            for i in range(length//2):
                if head.val==stack[-1]:
                    stack.pop()
                head=head.next
           
        else:
            for i in range(length//2):
                stack.append(head.val)
                head=head.next
            head=head.next
            for i in range(length//2):
                if head.val==stack[-1]:
                    stack.pop()
                head=head.next
        if stack:
            return False
        return True
