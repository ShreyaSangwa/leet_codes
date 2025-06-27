class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary(nums,low,high,key):
            mid=(high+low)//2
            if high<low:
                return -1
            if nums[mid]==key:
                return mid
            if nums[mid]<key:
                return binary(nums,mid+1,high,key)
            return binary(nums,low,mid-1,key)
        if nums==[]:
            return [-1,-1]
        a=[]
        if target not in nums:
            return [-1,-1]
        val=binary(nums,0,len(nums)-1,target)
        if val-1>-1 and nums[val-1]==target:
            while val-1>-1 and nums[val-1]==target:
                val-=1
            a.append(val)
        else:
            a.append(val)
        if val+1<len(nums) and nums[val+1]==target:
            while val<len(nums)-1 and nums[val+1]==target:
                val+=1
            a.append(val)
        else:
            a.append(val)
        return a