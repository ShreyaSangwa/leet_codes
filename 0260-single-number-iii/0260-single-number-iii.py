class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        i=0
        while i<len(nums)-1:
            if nums[i]!=nums[i+1]:
                ans.append(nums[i])
                i+=1
            else:
                i+=2
        if len(ans)!=2:
            ans.append(nums[i])
        return ans