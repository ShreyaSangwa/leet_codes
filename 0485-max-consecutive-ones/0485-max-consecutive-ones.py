class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxval=0
        i=0
        j=0
        while j<len(nums):
            while i<len(nums) and nums[i]==0:
                i+=1
            j=i
            while j<len(nums) and nums[j]==1:
                j+=1
            maxval=max(maxval, j-i)
            i=j
        return maxval