class Solution:
    def compress(self, chars: List[str]) -> int:
        a=0
        j=0
        if len(chars)==1:
            return len(chars)
        while a<len(chars):
            current_char= chars[a]
            count=0
            while a<len(chars) and chars[a]==current_char:
                count+=1
                a+=1
            chars[j]= current_char
            j+=1
            if count>1:
                for digit in str(count):
                    chars[j] = digit
                    j+=1
        chars=chars[:j]
        return len(chars)