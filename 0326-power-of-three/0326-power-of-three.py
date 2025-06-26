class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        if n<3:
            return False
        i=1
        while i<n:
            i*=3
        if i==n:
            return True
        return False