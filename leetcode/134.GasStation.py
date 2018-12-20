class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        dp = [gas[0] - cost[0]]
        for i in range(1,n):
            dp.append(dp[i-1] + gas[i] - cost[i])
        if dp[-1] < 0:
            return -1
        return (dp.index(min(dp)) + 1)%n


gas  = [3,1,1]
cost = [1,2,2]
print(Solution().canCompleteCircuit(gas, cost))
