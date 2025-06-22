class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        length = len(s)
        if length==k:
            return [s]
        if length<k:
            while length!=k:
                s+=fill
                length=len(s)
            return [s]
        a=list(s)
        i=0
        b=[]
        while i<length:
            j=0
            t=""
            while j<k and i+j<length:
                t+=a[i+j]
                j+=1
            b.append(t)
            i+=k
        a=b.pop()
        while len(a)<k:
            a+=fill
        b.append(a)
        return b