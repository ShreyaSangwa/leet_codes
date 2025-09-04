class Solution:
    def countAndSay(self, n: int) -> str:
        d="1"
        for i in range(n-1):
            c=""
            count=1
            for j in range(1,len(d)):
                if d[j-1]==d[j]:
                    count+=1
                else:
                    c+=str(count)+d[j-1]
                    count=1
            c+=str(count)+d[-1]
            d=c
        return d