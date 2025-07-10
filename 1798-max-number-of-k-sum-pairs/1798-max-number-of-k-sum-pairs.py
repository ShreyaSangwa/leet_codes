class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=0
        nums.sort()
        i=0
        j=len(nums)-1
        while nums[j]>k and j>0:
            j-=1
        while i<j:
            s=nums[i]+nums[j]
            if s==k:
                count+=1
                i+=1
                j-=1
            elif s>k:
                j-=1
            else:
                i+=1
        return count