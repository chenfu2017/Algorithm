class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        flag = False
        if x <0:
            x = -x
            flag = True
        while x:
            t = x%10
            x = x//10
            res = res*10+t
        if flag:
            res=-res
        if abs(res) > 2 ** 31:
            return 0
        return res

print(Solution().reverse(1534236469))


