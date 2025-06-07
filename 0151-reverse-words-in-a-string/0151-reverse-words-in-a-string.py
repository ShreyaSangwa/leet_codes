class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        for i in range(len(a)//2):
            temp=a[i]
            a[i]=a[len(a)-i-1]
            a[len(a)-i-1]=temp
        b=" ".join(a)
        return b
