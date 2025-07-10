class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        a=Counter(arr)
        b=list(a.values())
        b.sort(reverse=True)
        count=0
        val=len(arr)
        while val>len(arr)//2:
            val-=b[count]
            count+=1
        return count