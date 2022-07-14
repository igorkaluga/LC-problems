class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        
        ar = ["+", "-", "*", "/"]
        for i in tokens:
            if i not in ar:
                stack.append(i)
            else:
                if i == "/":
                    stack[-2] = str(int(eval("".join([stack[-2], i, stack[-1]]))))
                    stack.pop()
                    continue
                stack[-2] = str(eval("".join([stack[-2], i, stack[-1]])))
                stack.pop()

        return int(stack[0])
        
#This was the original solution I was trying to work out
#the string manipulation makes this run a lot slower than the first solution
#(wanted to include for reference later on)        
