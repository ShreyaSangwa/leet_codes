class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        a=1
        b=2
        for i in range(3,n+1):
            temp=a
            a=b
            b=temp+b
        return b