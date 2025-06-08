class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        a=[]
        for i in range(1,n+1):
            a.append(str(i))
        a.sort()
        a=[int(i) for i in a]
        return a