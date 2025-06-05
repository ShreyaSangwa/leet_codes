class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        a=[]
        alt=groups[0]
        if len(words)==1:
            return words
        else:
            for i in range(len(words)):
                if groups[i]==alt:
                    a.append(words[i])
                    if alt==0:
                        alt=1
                    else:
                        alt=0
            return a

