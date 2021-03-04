from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = buy2 = prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = min(buy1, prices[i])
            sell1 = max(sell1, prices[i] - buy1)
            buy2 = min(buy2, prices[i] - sell1)
            sell2 = max(sell2,prices[i]- buy2)
        return sell2


prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(Solution().maxProfit(prices))
