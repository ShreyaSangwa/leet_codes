# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            a=ListNode()
            temp=a
            while list1 and list2:
                if list1.val<=list2.val:
                    temp.next=ListNode(list1.val)
                    list1=list1.next
                else:
                    temp.next=ListNode(list2.val)
                    list2=list2.next
                temp=temp.next
            temp.next=list1 or list2
            return a.next