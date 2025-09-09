class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        know = deque([(1,1)])
        share=deque([])
        kcount=1
        scount=0
        for i in range (2,n+1):
            if know and (know[0][0]==i-delay):
                kcount-=know[0][1]
                scount+=know[0][1]
                share.append(know[0])
                know.popleft()
            if share and (share[0][0]==i-forget):
                scount-=share[0][1]
                share.popleft()
            if share:
                kcount+=scount
                know.append((i,scount))
        return (kcount+scount)%(pow(10,9)+7)