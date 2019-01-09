class Solution:

    def interval_sum_1(self, num):
        res = float('-INF')
        dp = [0] * len(num)
        dp[0] = [0, num[0]][num[0] > 0]
        for i in range(1, len(num)):
            dp[i] = max(dp[i - 1] + num[i], num[i])
            res = max(res, dp[i])
        print(dp)
        return res

    def interval_sum_2(self, num):
        res = float('-INF')
        b = 0
        for i in num:
            if b > 0:
                b += i
                res = max(b, res)
            else:
                b = i
            print(b,end=' ')
        print()
        return res


num = [-2, 11, -12, 15, -6, 5, 10, - 2]
print(Solution().interval_sum_2(num))
