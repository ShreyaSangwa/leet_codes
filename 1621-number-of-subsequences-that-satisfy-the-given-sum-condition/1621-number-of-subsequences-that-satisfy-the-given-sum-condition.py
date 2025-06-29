class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        length=len(nums)
        left=0
        right=length-1
        count=0
        while left<=right:
            if nums[left]+nums[right]<=target:
                count+= pow(2,right-left)
                count=count%(10**9+7)
                left+=1
            else:
                right-=1
        return count