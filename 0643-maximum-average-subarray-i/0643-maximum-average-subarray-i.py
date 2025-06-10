class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr=sum(nums[:k])
        maxval=curr
        for i in range(k,len(nums)):
            curr=curr+nums[i]-nums[i-k]
            maxval=max(maxval,curr)
        return maxval/k