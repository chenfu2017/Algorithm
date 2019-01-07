class Solution:

    def interval_sum(self, num):
        res = float('-INF')
        dp = [0] * len(num)
        dp[0] = [0, num[0]][num[0] > 0]
        for i in range(1, len(num)):
            dp[i] = max(dp[i - 1] + num[i], num[i])
            res = max(res, dp[i])
        print(dp)
        return res


num = [-2, 11, -12, 15, -6, 5, 10 - 2]
print(Solution().interval_sum(num))
