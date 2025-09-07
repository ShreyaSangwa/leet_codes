class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n==1:
            return [0]
        a=[]
        if n%2==0:
            n=int(n/2)
            for i in range(1,n+1):
                a.append(i)
                a.append(-i)
        else:
            n=int((n-1)/2)
            for i in range(1,n+1):
                a.append(i)
                a.append(-i)
            a.append(0)
        return a