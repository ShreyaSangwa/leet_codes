class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def push(a:List[int],val):
            if len(a)==0:
                a.append(val)
            elif a[-1]<0:
                a.append(val)
            else:
                if val>0:
                    a.append(val)
                else:
                    y=a.pop()
                    if abs(y)>abs(val):
                        push(a,y)
                    elif abs(y)<abs(val):
                        push(a,val)
        a=[]
        for i in asteroids:
            push(a,i)
        return a