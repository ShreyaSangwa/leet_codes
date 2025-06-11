class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=["+","-","*","/"]
        stack=[]
        for i in tokens:
            if i in a:
                num2=stack.pop()
                num1=stack.pop()
                if i=="+":
                    val=num1+num2
                    stack.append(val)
                elif i=="-":
                    val=num1-num2
                    stack.append(val)
                elif i=="*":
                    val=num1*num2
                    stack.append(val)
                else:
                    val=num1/num2
                    stack.append(int(val))
            else:
                stack.append(int(i))
        return int(stack.pop())
        