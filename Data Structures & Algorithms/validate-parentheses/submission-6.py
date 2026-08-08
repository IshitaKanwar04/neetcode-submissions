class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = ['(','[','{']
        if not s[0] in open_brackets:
            return False
        b_dict = {'{':'}', '(':')', '[':']'} 
        for i in range(len(s)):
            if s[i] in open_brackets:
                stack.append(s[i])
            elif len(stack) and b_dict[stack[-1]] == s[i]:
                    stack.pop()
            else:
                return False

        return len(stack) == 0
                
        