class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        filled=numBottles
        ans=numBottles
        empty=0
        while filled!=0:
            empty+=filled
            filled=empty//numExchange
            empty=empty%numExchange
            ans+=filled
        return ans