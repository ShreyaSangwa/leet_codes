class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        a=len(nums1)
        b=len(nums2)
        if a>b:
            c=[]
            for i in nums1:
                if i in nums2:
                    c.append(i)
            return list(set(c))
        else:
            c=[]
            for i in nums2:
                if i in nums1:
                    c.append(i)
            return list(set(c))