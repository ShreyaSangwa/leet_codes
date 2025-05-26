class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0]==nums[1] and nums[1]==nums[2]:
            return "equilateral"
        else:
            if nums[0]+nums[1]>nums[2] and nums[1]+nums[2]>nums[0] and nums[2]+nums[0]>nums[1]:
                if nums[0]!=nums[1] and nums[1]!=nums[2] and nums[2]!=nums[0]:
                    return "scalene"
                else:
                    return "isosceles"
            else:
                return "none"