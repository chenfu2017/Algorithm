from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        n = len(coins)
        for i in range(1, amount + 1):
            for j in range(n):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return [dp[amount],-1][dp[amount]==float('inf')]


coins = [2]
amount = 3
print(Solution().coinChange(coins, amount))
