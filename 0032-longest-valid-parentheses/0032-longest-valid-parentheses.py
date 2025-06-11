class Solution:
    def longestValidParentheses(self, s: str) -> int:
        a=[]
        b=["0" for i in range(len(s))]
        for i in range(len(s)):
            if s[i]=="(":
                a.append(i)
            elif a:
                print(2)
                index=a.pop()
                b[index]=1
                b[i]=1
        print(b)
        maxval=0
        length=0
        for i in b:
            if i==1:
                length+=1
            else:
                maxval=max(length,maxval)
                length=0
        maxval=max(length,maxval)
        return maxval