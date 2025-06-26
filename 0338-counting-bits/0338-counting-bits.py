class Solution:
    def countBits(self, n: int) -> List[int]:
        b=[]
        for i in range(n+1):
            a=bin(i)
            count=a[2:].count("1")
            b.append(count)
        return b