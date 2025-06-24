class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        n=str(bin(n))
        if n.count('1')==1:
            return True
        return False