class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        final=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j]==key and abs(i-j)<=k:
                    final.append(i)
                    break
        return final