class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        brackets = {"{" : "}", "(" : ")", "[" : "]"}
        for char in s:
            if char in brackets:
                stack.append(char)
            elif stack and char == brackets[stack.pop()]:
                pass
            else:
                return False

        if stack:
            return False
        return True
                