class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pi=-1

        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                pi=i
                break
        if pi==-1:
            nums.reverse()
            return
        for i in range(len(nums)-1,pi,-1):
            if nums[pi]<nums[i]:
                nums[pi],nums[i]=nums[i],nums[pi]
                break
        left=pi+1
        right=len(nums)-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1