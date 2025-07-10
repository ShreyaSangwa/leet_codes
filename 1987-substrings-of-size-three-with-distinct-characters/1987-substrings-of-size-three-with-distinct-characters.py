class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s)<3:
            return 0
        def good(s):
            a=Counter(s)
            for i in a:
                if a[i]>1:
                    return False
            return True
        i=0
        j=2
        count=0
        while j<len(s):
            if good(s[i:j+1]):
                count+=1
            i+=1
            j+=1
        return count