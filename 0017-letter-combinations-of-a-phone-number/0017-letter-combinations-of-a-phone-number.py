class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums=[2,3,4,5,6,7,8,9]
        vals=[['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        final=[]
        for i in digits:
            if int(i) in nums:
                final.append(vals[nums.index(int(i))])
        def join(l1,l2):
            result=[]
            for i in l1:
                for j in l2:
                    result.append(i+j)
            return result
        if final==[]:
            return final
        while len(final)>=2:
            l2=final.pop()
            l1=final.pop()
            final.append(join(l1,l2))
        return final[0]