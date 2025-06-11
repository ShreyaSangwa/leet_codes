class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        if len(s)%2!=0:
            return False
        for i in s:
            if i=="[" or i=="{" or i=="(":
                a.append(i)
            elif i=="]":
                if len(a)>0 and a[-1]=="[":
                    a.pop()
                else:
                    return False
            elif len(a)>0 and i=="}":
                if a[-1]=="{":
                    a.pop()
                else:
                    return False
            elif len(a)>0 and i==")":
                if a[-1]=="(":
                    a.pop()
                else:
                    return False
            else:
                return False
        if len(a)==0:
            return True
        return False