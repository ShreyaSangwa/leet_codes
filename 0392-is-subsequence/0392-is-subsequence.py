class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a=len(s)
        b=len(t)
        j=0
        count=0
        if a==0:
            return True
        for i in range(b):
            if j==a:
                break
            if s[j]==t[i] and j<a:
                count+=1
                j+=1
        if count == a:
            return True
        return False