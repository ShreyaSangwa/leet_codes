class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        while i<len(nums) and nums[i]<1:
            i+=1
        if i==len(nums):
            return 1
        if nums[i]!=1:
            return 1
        while i+1<len(nums) and (nums[i]+1==nums[i+1] or nums[i]==nums[i+1]):
            i+=1
        return nums[i]+1