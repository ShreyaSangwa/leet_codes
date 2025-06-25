class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        if len(nums)==1:
            return [str(nums[0])]
        a=[]
        b=[]
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                b.append(nums[i])
            else:
                b.append(nums[i])
                a.append(b)
                b=[]
        if b==[]:
            b.append(nums[i+1])
            a.append(b)
        elif b[-1]+1==nums[i+1]:
            b.append(nums[i+1])
            a.append(b)
        b=[]
        for i in a:
            if len(i)==1:
                b.append(str(i[0]))
            else:
                b.append(str(i[0])+"->"+str(i[-1]))
        return b