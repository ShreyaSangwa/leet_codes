class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        while len(nums)>k:
            val=min(nums)
            nums.remove(val)
        return nums