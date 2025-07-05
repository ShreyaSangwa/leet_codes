class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        a=list(d.keys())
        a=sorted(a,reverse=True)
        d={i:d[i] for i in a}
        for i in d:
            if i==d[i]:
                return i
        return -1