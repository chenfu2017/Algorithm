class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]
    # val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    # sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    #
    # def intToRoman(self, num):
    #     """
    #     :type num: int
    #     :rtype: str
    #     """
    #     s = ""
    #     i = 0
    #     while i!=len(self.val):
    #         if num // self.val[i] >= 1:
    #             s += self.sym[i]
    #             num -= self.val[i]
    #         else:
    #             i += 1
    #     return s


print(Solution().intToRoman(3))
