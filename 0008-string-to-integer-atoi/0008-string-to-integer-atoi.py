class Solution:
    def myAtoi(self, s: str) -> int:
        a=list(s)
        num=0
        i=0
        neg = 0
        while a and a[0]==" ":
            a.remove(" ")
        if a==[]:
            return 0
        if a[i]=="+":
            i+=1
            neg = 0
        elif a[i]=="-":
            i+=1
            neg = 1
        while i<len(a):
            if a[i].isdigit(): 
                num = num*10 + int(a[i])
            else:
                break
            i+=1
        if neg:
            num = -num
        else:
            num = num
        if num>(pow(2,31)-1):
            return pow(2,31)-1
        elif num<(-pow(2,31)):
            return -pow(2,31)
        else:
            return num