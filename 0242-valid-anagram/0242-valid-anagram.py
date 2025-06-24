class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd={}
        td={}
        for i in range(len(s)):
            if s[i] in sd:
                sd[s[i]]+=1
            else:
                sd[s[i]]=1
        for i in range(len(t)):
            if t[i] in td:
                td[t[i]]+=1
            else:
                td[t[i]]=1
        myKeys = list(sd.keys())
        myKeys.sort()   
        sd = {i: sd[i] for i in myKeys}
        myKeys = list(td.keys())
        myKeys.sort()   
        td = {i: td[i] for i in myKeys}
        print(sd,td)
        return sd==td