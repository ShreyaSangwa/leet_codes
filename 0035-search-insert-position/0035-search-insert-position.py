class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high=len(nums)
        low=0
        mid=0
        while target!=nums[mid] and low<high:
            mid=(high+low)//2
            if target>nums[mid]:
                low=mid+1
            else:
                high=mid-1
        if target==nums[mid]:
            return mid
        else:
            i=0
            while i<len(nums) and target>nums[i] :
                i+=1
            return i