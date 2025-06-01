class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word=""
        for i in range(min(len(word1),len(word2))):
            word+=word1[i]+word2[i]
        if len(word1)!=len(word2):
            if len(word1)>len(word2):
                word+=word1[i+1:len(word1)]
            else:
                word+=word2[i+1:len(word2)]
        return word