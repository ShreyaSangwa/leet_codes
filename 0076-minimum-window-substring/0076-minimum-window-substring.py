class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(sc,tc):
            for i in tc:
                if sc[i]<tc[i]:
                    return False
            return True
        tc=Counter(t)
        sc=Counter()
        i=0
        result=""
        min_len=float("inf")
        for j in range(len(s)):
            sc[s[j]]+=1
            while check(sc,tc):
                if j-i+1<min_len:
                    result=s[i:j+1]
                    min_len=j-i+1
                sc[s[i]]-=1
                i+=1
        return result