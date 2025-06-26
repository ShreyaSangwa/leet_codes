class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        i=0
        j=len(s)-1
        a=["a","e","i","o","u","A","E","I","O","U"]
        while i<j:
            if s[i] not in a:
                i+=1
            if s[j] not in a:
                j-=1
            if s[i] in a and s[j] in a:
                temp=s[i]
                s[i]=s[j]
                s[j]=temp
                i+=1
                j-=1
        return "".join(s)