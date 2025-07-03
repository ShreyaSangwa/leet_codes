class Solution:
    def kthCharacter(self, k: int) -> str:
        word='a'
        while len(word)<k:
            b=''
            for i in word:
                if i=='z':
                    b+='a'
                else:
                    val=ord(i)
                    b+=chr(val+1)
            word+=b
        return word[k-1]        