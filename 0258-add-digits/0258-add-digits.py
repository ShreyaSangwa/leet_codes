class Solution:
    def addDigits(self, num: int) -> int:
        a=str(num)
        while len(a)!=1:
            sum=0
            for i in a:
                sum+=int(i)
            a=str(sum)
        return int(a)