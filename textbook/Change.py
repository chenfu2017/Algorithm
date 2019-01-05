class Solution:

    def change(self, money):
        """
        :param money:以分为单位
        :return:
        """
        m = (100, 50, 10, 5, 2, 1)
        n = len(m)
        res = [0] * n
        for i in range(n):
            while money >= m[i]:
                money -= m[i]
                res[i] += 1
        for i in range(n):
            if res[i]:
                print("%d:%d张" % (m[i], res[i]),end='   ')


Solution().change(205)
