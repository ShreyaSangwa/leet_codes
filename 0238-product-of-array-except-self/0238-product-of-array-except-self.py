class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[0 for i in range(len(nums))]
        b=1
        for i in range(0,len(nums)):
            a[i]=b
            b*=nums[i]
        c=1
        for i in range(len(nums)-1,-1,-1):
            a[i]=c*a[i]
            c*=nums[i]
        return a