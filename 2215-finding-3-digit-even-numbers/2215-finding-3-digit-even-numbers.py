from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        b=[]
        a=[subset for subset in list(set(permutations(digits,3))) if (subset[2]%2==0 and subset[0]!=0)]
        
        for i in a:
            c=''.join(map(str,i))
            b.append(int(c))
        b.sort()
        return b