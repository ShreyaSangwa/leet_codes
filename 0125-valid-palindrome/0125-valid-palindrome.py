class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in s:
            if i.isalnum():
                a+=i
            else:continue
        a=a.lower()
        b=a[::-1]
        print(a,b)
        return a==b