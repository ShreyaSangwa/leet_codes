class Solution:
    def reverse(self, x: int) -> int:
        a=0
        if x<0:
            x=-x
            while x!=0:
                a=(a*10)+(x%10)
                x=x//10
            a=-a
        else:
            while x!=0:
                a=(a*10)+(x%10)
                x=x//10
        if(a>pow(2,31)-1) or (a<-pow(2,31)):
            return 0
        else:
            return a
