class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = ["+", "-", "*", "/"]
        stack = []
        
        for token in tokens:

            if token not in operators:

                stack.append(token)

            else:

                if token == "+":

                    result = int(stack[-2]) + int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(str(result))

                elif token == "-":

                    result = int(stack[-2]) - int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(str(result))

                elif token == "*":

                    result = int(stack[-2]) * int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(str(result))

                elif token == "/":

                    result = int(int(stack[-2])/int(stack[-1]))
                    stack.pop()
                    stack.pop()
                    stack.append(str(result))
        
        return int(stack[0])

