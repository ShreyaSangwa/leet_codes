class Solution:
    def countAndSay(self, n: int) -> str:
        d="1"
        for i in range(n-1):
            c=""
            count=1
            a=d[0]
            j=1
            while j<len(d):
                if a==d[j]:
                    count+=1
                else:
                    c+=str(count)+d[j-1]
                    count=1
                    a=d[j]
                j+=1
            c+=str(count)+d[j-1]
            d=c
        return d