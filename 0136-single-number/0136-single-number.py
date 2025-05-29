class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==1:
            return nums[0]
        for i in range(0, len(nums)-1, 2):
            if nums[i] ^ nums[i+1]:
                return nums[i]
        if nums[len(nums)-1] ^ nums[len(nums)-2]:
            return nums[len(nums)-1]    