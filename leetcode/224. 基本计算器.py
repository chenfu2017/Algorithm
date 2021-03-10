class Solution:
    def checkpriority(self, op1, op2):
        d = {'+': 0, '-': 1, '(': 2, ')': 3, '#': 4}
        priority = [
            [1, 1, -1, 1, -1],
            [1, 1, -1, 1, -1],
            [-1, -1, -1, 0, -1],
            [1, 1, 0, 1, 1]
        ]
        return priority[d[op1]][d[op2]]

    def addorsub(self,stack,operator):
        o = operator.pop()
        a = stack.pop()
        b = stack.pop()
        if o == '+':
            stack.append(b + a)
        else:
            stack.append(b - a)

    def calculate(self, s: str) -> int:
        s = s.strip()
        if s[0] == '-':
            s = '0' + s
        s = s.replace('(-', '(0-')
        stack = []
        operator = ['#']
        i = 0
        n = len(s)
        while i < n:
            c = s[i]
            if c == '+' or c == '-' or c == '(' or c == ')':
                while self.checkpriority(c, operator[-1]) > 0:
                    self.addorsub(stack,operator)
                if c == ')':
                    operator.pop()
                else:
                    operator.append(c)
                i += 1
            elif c != ' ':
                num = 0
                while i < n and '0' <= s[i] <= '9':
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                stack.append(num)
            else:
                i += 1
        while operator[-1] != '#':
            self.addorsub(stack,operator)
        return stack[-1]


s = " -2 + (-3+2+1) + (-31 + 2+1111)"
print(Solution().calculate(s))
