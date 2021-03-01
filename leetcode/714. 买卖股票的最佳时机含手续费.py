from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        temp = prices[0]
        n = len(prices)
        i = 1
        ans = 0
        while i < n:
            if prices[i] < temp:
                temp = prices[i]
            elif prices[i] - temp > fee:
                ans += prices[i] - temp - fee
                temp = prices[i] - fee
            i += 1
        return ans


prices = [1,3,7,5,10,3]
fee = 3
print(Solution().maxProfit(prices, fee))
