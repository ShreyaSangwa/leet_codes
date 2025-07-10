class Solution:
    def reorganizeString(self, s: str) -> str:
        a=Counter(s)
        a={k:v for k,v in sorted(a.items(),key=lambda item:item[1],reverse=True)}
        b=[""]*len(s)
        j=0
        for i in a:
            if len(s)%2==0 and a[i]>len(s)//2:
                return ""
            if len(s)%2!=0 and a[i]>len(s)//2+1:
                return ""
            while j<len(s) and a[i]>0:
                b[j]=i
                j+=2
                a[i]-=1
            if j>=len(s):
                j=1
            if a[i]>0:
                while j<len(s) and a[i]>0:
                    b[j]=i
                    j+=2
                    a[i]-=1
        return "".join(b)