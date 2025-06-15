class Solution:
    def maxDiff(self, num: int) -> int:
        maxval=''
        minval=''
        num=str(num)
        i=0
        if num[0]=='9':
            while i<len(num):
                if num[i]=='9':
                    maxval+='9'
                    minval+='1'
                    i+=1
                else:
                    break
            if i<len(num):
                val=num[i]
                while i<len(num):
                    if num[i]==val:
                        maxval+='9'
                        minval+=val
                    elif num[i]=='9':
                        minval+='1'
                        maxval+='9'
                    else:
                        minval+=num[i]
                        maxval+=num[i]
                    i+=1
        elif num[i]=='1':
            i=0
            while i<len(num):
                if num[i]=='1':
                    minval+='1'
                    maxval+='9'
                    i+=1
                else:
                    break
            if i <len(num):
                if num[i]=='0':
                    while i<len(num) and (num[i]=='0' or num[i]=='1'):
                        if num[i]=='0':
                            minval+='0'
                            maxval+='0'
                        elif num[i]=='1':
                            minval+='1'
                            maxval+='9'
                        else:
                            break
                
                        i+=1
                if i<len(num):
                    val=num[i]
                    while i <len(num):
                        if num[i]==val:
                            minval+='0'
                            maxval+=num[i]
                        elif num[i]=='1':
                            minval+='1'
                            maxval+='9'
                        else:
                            minval+=num[i]
                            maxval+=num[i]
                        i+=1
        else:
            i=0
            while i <len(num):
                if num[i]==num[0]:
                    minval+='1'
                    maxval+='9'
                else:
                    minval+=num[i]
                    maxval+=num[i]
                i+=1
        print(minval,maxval)
        return int(maxval)-int(minval)