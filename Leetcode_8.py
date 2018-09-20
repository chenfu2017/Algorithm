class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str
        s = s.strip(' ')
        if len(s) == 0:
            return 0
        sign = -1 if s[0] == '-' else 1
        if s[0] in '+-':
            s = s[1:]
        res = 0
        for digit in s:
            if not digit.isdigit():
                break
            res = res * 10 + int(digit)
        return min(max(res * sign, -2 ** 31), 2 ** 31 - 1)
