class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def nd(arr):
            for i in range(len(arr)-1):
                if arr[i]>arr[i+1]:
                    return False
            return True
        op=0
        while not nd(nums):
            min_sum=999999
            index=0
            for i in range(len(nums)-1):
                summ=nums[i]+nums[i+1]
                if summ<min_sum:
                    min_sum=summ
                    index=i
            nums = nums[:index]+[min_sum]+nums[index+2:]
            op+=1
        return op