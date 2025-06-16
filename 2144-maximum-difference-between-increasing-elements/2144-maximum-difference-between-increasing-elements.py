class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diffMax = -1
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j]-nums[i]>diffMax:
                    print(nums[i],nums[j])
                    diffMax = nums[j]-nums[i]
        if diffMax==0:
            return -1
        return diffMax