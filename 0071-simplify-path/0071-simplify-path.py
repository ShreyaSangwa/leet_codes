class Solution:
    def simplifyPath(self, path: str) -> str:
        a=path.split("/")
        b=[]
        for i in a:
            if i=='' or i=='.':
                continue
            elif i=='..':
                if b:
                    b.pop()
            else:
                b.append(i)
        result=""
        if b:
            for i in b:
                result+="/"+i
            return result
        else:
            return "/"