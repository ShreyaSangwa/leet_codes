class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a=sum(nums)
        sumleft=0
        for i in range(len(nums)):
            a=a-nums[i]
            if(sumleft==a):
                return i
            sumleft+=nums[i]
        return -1