class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        filled=numBottles
        ans=numBottles
        empty=0
        empty=filled
        filled=0
        while empty>=numExchange:
            empty=empty-numExchange
            numExchange+=1
            filled=1
            ans+=filled
            empty+=filled
            filled=0
        return ans