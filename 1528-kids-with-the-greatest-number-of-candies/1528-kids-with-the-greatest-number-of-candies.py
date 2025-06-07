class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=[]
        for i in range(len(candies)):
            temp=candies[i]
            candies[i]+=extraCandies
            if candies[i]==max(candies):
                a.append(True)
            else:
                a.append(False)
            candies[i]=temp
        return a