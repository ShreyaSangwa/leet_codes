# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cp=[]
        i=head
        j=head.next
        index=1
        while(j.next!=None):
            if (i.val<j.val and j.val>j.next.val)or(i.val>j.val and j.val<j.next.val):
               cp.append(index)
            i=j
            j=j.next
            index+=1
        print(cp)
        if len(cp)<2:
            return [-1,-1]
        else:
            maxd=max(cp)-min(cp)
            mini=abs(cp[0]-cp[1])
            for i in range(1,len(cp)-1):
                if (cp[i+1]-cp[i])<mini:
                    mini=cp[i+1]-cp[i]
            bleh=[mini,maxd]
            return bleh