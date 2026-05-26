class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            print(stack)
            if i == "+":
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(a + b)
            elif i == "/":
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b / a)
            elif i == "-":
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b - a)
            elif i == "*":
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(a * b)
            else:
                stack.append(i)
        return int(stack[-1])