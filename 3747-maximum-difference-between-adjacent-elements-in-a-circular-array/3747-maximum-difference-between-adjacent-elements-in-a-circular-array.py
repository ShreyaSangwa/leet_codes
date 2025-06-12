class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxval=0
        for i in range(len(nums)-1):
            diff=abs(nums[i]-nums[i+1])
            if diff>maxval:
                maxval=diff
        diff=abs(nums[0]-nums[-1])
        if diff>maxval:
            maxval=diff
        return maxval