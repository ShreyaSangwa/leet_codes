class Solution:
    def convert(self, s: str, numRows: int) -> str:
        a = [""]*numRows
        index = 0
        fwd = 1
        for i in range(len(s)):
            a[index]+=s[i]
            if((index<numRows-1 and fwd==1) or (index>0 and fwd==-1)):
                pass
            else:
                fwd=-fwd
            index+=fwd
        return "".join(a)
        