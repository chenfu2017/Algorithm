from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackvalue = []
        for str in tokens:
            if str == '+':
                a = stackvalue.pop()
                b = stackvalue.pop()
                stackvalue.append(a + b)
            elif str == '-':
                a = stackvalue.pop()
                b = stackvalue.pop()
                stackvalue.append(b - a)
            elif str == '*':
                a = stackvalue.pop()
                b = stackvalue.pop()
                stackvalue.append(a * b)
            elif str == '/':
                a = stackvalue.pop()
                b = stackvalue.pop()
                stackvalue.append(int(b /a))
            else:
                stackvalue.append(int(str))
        return stackvalue.pop()


nums = ["4","-2","/","2","-3","-","-"]
print(Solution().evalRPN(nums))
