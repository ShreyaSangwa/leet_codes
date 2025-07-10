class Solution:
    def minDeletions(self, s: str) -> int:
        a=Counter(s)
        b=list(a.values())
        c=b.copy()
        deletions=0
        for i in b:
            c.remove(i)
            while i in c:
                i-=1
                deletions+=1
            if i!=0:
                c.append(i)
        return deletions