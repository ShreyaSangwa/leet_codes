class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=""
        length=len(strs[0])
        for i in strs:
            if len(i)<length:
                length=len(i)
        for i in range(length):
            for j in range(1,len(strs)):
                if strs[0][i]!=strs[j][i]:
                    return a
            a+=strs[0][i]
        return a
