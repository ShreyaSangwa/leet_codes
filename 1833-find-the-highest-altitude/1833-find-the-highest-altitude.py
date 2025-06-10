class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=[0]
        sum=0
        for i in range(len(gain)):
            sum+=gain[i]
            a.append(sum)
        b=max(a)
        return b