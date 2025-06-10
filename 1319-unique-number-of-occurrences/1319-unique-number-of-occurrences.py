class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        arr=[]
        for i in d:
            if d[i] in arr:
                return False
            else:
                arr.append(d[i])
        return True