class Solution:
    def hammingWeight(self, n: int) -> int:
        a=0
        while n>0:
            a=a*10+n%2
            n=n//2
        val=0
        for i in str(a):
            if i=='1':
                val+=1
            else:
                continue
        return val