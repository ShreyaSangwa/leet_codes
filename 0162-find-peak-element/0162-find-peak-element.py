class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binary(nums,low,high):
            mid=(low+high)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            if nums[mid]>nums[mid-1]:
                return binary(nums,mid+1,high)
            return binary(nums,low,mid-1)
        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return len(nums)-1
        return binary(nums,1,len(nums)-2)