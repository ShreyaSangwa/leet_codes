class Solution:
    def minMaxDifference(self, num: int) -> int:
        maxval=''
        minval=''
        a=str(num)
        i=0
        if a[i]=='9':
            while i< len(a) and a[i]=='9':
                maxval+='9'
                i+=1
            if i<len(a):
                val=a[i]
                while i<len(a):
                    if a[i]==val:
                        maxval+='9'
                    else:
                        maxval+=a[i]
                    i+=1
            for i in a:
                if i==a[0]:
                    minval+='0'
                else:
                    minval+=i
        elif a[i]=='0':
            while i< len(a) and a[i]=='0':
                minval+='0'
                i+=1
            if i<len(a):
                val=a[i]
                while i<len(a):
                    if a[i]==val:
                        minval+='0'
                    else:
                        minval+=a[i]
                    i+=1
            for i in a:
                if i==a[0]:
                    maxval+='9'
                else:
                    maxval+=i
        else:
            for i in a:
                if i==a[0]:
                    minval+='0'
                    maxval+='9'
                else:
                    maxval+=i
                    minval+=i        
        return int(maxval)-int(minval)