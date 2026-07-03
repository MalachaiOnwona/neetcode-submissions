class Solution:
    def isValid(self, s: str) -> bool:

        matches = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for char in s:

            if char in matches:

                if stack and stack[-1] == matches[char]:

                    stack.pop()

                else:
                    return False
            
            else:

                stack.append(char)
        
        # Stack should be empty at the end if all open brackets had 
        # matching closing brackets
        if not stack:
            return True
        else:
            return False
        