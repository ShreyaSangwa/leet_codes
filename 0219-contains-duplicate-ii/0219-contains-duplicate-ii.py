class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]]=[i]
        for i in d:
            if len(d[i])>1:
                for j in range(len(d[i])-1):
                    if abs(d[i][j]-d[i][j+1])<=k:
                        return True
        return False