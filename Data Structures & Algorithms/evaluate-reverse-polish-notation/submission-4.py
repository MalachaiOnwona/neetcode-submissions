class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operators = ["+", "-", "*", "/"]
        result = 0

        for token in tokens:

            if token not in operators:

                stack.append(int(token))

            else:

                if token == "+":

                    result = stack.pop() + stack.pop()
                    stack.append(result)
                
                elif token == "-":

                    last = stack.pop()
                    second_to_last = stack.pop()

                    result = second_to_last - last
                    stack.append(result)

                elif token == "*":

                    result = stack.pop() * stack.pop()
                    stack.append(result)

                elif token == "/":

                    last = stack.pop()
                    second_to_last = stack.pop()

                    result = int(second_to_last/last)
                    stack.append(result)
        
        return stack[0]


        