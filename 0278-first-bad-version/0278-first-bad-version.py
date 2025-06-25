# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n==1:
            return 1
        high=n
        low=1
        mid=(high+low)//2
        while not (isBadVersion(mid)==True and isBadVersion(mid-1)==False):
            if isBadVersion(mid)==False:
                low=mid+1
                mid=(high+low)//2
            else:
                high=mid-1
                mid=(high+low)//2
        return mid