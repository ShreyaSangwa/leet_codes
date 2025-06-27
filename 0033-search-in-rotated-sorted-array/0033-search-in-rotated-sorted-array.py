class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(nums,high,low,key):
            mid=(high+low)//2
            if high<low:
                return -1
            if nums[mid]==key:
                return mid
            if nums[low]<=nums[mid]:
                if key<nums[low] or key>nums[mid]:
                    return binary(nums,high,mid+1,key)
                return binary(nums,mid-1,low,key)
            if key>nums[high] or key<nums[mid]:
                return binary(nums,mid-1,low,key)
            return binary(nums,high,mid+1,key)
        return binary(nums,len(nums)-1,0,target)