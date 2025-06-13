class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k=0
        if len(haystack)<len(needle):
            return -1
        if len(haystack)==len(needle):
            if haystack==needle:
                return 0
            return -1
        for i in range(len(haystack)-len(needle)):
            if haystack[i]==needle[k]:
                temp=i
                while haystack[i]==needle[k]:
                    i+=1
                    k+=1
                    if k==len(needle):
                        return temp
                k=0
        k=0
        while haystack[len(haystack)-len(needle)+k]==needle[k]:
            k+=1
            if k==len(needle):
                return len(haystack)-len(needle)
        return -1                    