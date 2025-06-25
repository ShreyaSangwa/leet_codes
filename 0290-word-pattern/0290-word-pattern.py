class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a=s.split()
        if len(a)!=len(pattern):
            return False
        d={}
        for i in range(len(a)):
            if pattern[i] in d:
                if d[pattern[i]]!=a[i]:
                    return False
            else:
                d[pattern[i]]=a[i]
        a=list(d.values())
        a.sort()
        for i in range(len(a)-1):
            if a[i]==a[i+1]:
                return False
        return True