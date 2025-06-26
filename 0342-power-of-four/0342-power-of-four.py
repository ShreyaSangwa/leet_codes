class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        if n<4:
            return False
        i=1
        while i<n:
            i*=4
        if i==n:
            return True
        return False