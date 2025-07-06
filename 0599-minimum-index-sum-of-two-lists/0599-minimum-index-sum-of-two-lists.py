class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d={}
        for i in list1:
            if i in list2:
                val=list1.index(i)+list2.index(i)
                d[i]=val
        a=list(d.values())
        b=min(a)
        a=[]
        for i in d:
            if d[i]==b:
                a.append(i)
        return a