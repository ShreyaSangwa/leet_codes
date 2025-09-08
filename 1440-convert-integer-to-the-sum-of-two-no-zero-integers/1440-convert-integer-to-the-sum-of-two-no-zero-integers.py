class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        i=1
        while "0" in str(n-i) or "0" in str(i):
            i+=1
        return [i,n-i]