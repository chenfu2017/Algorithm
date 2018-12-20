class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum =0
        for i in range(1,len(prices)):
            if prices[i-1]<prices[i]:
                sum+=prices[i]-prices[i-1]
        return sum

nums=[7,1,5,3,6,4]
print(Solution().maxProfit(nums))

