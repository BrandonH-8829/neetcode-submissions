class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        if len(s) == 1:
            return True
        open_bracket = {"{":"}", "[":"]", "(":")"}
        stack = []
        for l in range(len(s)):
            if s[l] in open_bracket:
                print(f"Open Bracket {s[l]}")
                stack.append(s[l])
            else:
                print(f"closed Bracket {s[l]}")
                #print(f"urrent stack {stack[-1]}")
                if stack and s[l] == open_bracket[stack[-1]]:
                    stack.pop()
                else:
                    return False 
        return True if len(stack) == 0 else False