class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=list(set(nums))
        counter=[]
        for i in a:
            counter.append(nums.count(i))
        res=[]
        while len(res)<k:
            m=max(counter)
            i=counter.index(m)
            counter.remove(m)
            res.append(a[i])
            a.remove(a[i])
        return res