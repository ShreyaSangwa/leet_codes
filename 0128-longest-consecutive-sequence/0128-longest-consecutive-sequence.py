class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m=0
        nums=list(set(nums))
        nums.sort()
        print(nums)
        i=0
        while i<len(nums):
            count=1
            while i+1<len(nums):
                if nums[i]+1==nums[i+1]:
                    count+=1
                    i+=1
                else:
                    break
            i+=1
            if count>m:
                m=count
        return m
