class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        a=0
        ret=''
        for i in s[::-1]:
            if i=='-':
                continue
            else:
                if a!=k:
                    a+=1
                    ret+=i.upper()
                else:
                    ret+='-'
                    a=0
                    ret+=i.upper()
                    a+=1
        return ret[::-1]