class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        length=0
        extra=0
        dictionary=collections.Counter(words)
        for key in dictionary.keys():
            if key[0]==key[1]:
                if dictionary[key]%2==1:
                    extra = 1
                length+=(dictionary[key]//2)*4
            else:
                reverse=key[1]+key[0]
                length+=min(dictionary[key],dictionary[reverse])*2
        return length+(extra*2)