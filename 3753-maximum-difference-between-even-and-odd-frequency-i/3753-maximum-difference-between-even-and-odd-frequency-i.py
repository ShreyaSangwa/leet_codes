class Solution:
    def maxDifference(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        a=[]
        for i in d:
            a.append(d[i])
        a.sort()
        
        for i in a:
            if i%2==0:
                a2=i
                break
        for i in range(len(a)-1,-1,-1):
            if a[i]%2!=0:
                a1=a[i]
                break
        return a1-a2