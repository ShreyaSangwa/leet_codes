class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff=0
        minp=999999
        for i in range(len(prices)):
            if prices[i]<minp:
                minp = prices[i]
            else:
                diff = max(diff,prices[i]-minp)
        return diff