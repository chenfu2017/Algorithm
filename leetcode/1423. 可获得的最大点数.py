from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        length = n - k
        sumres = sum(cardPoints[:length])
        minnum = total = sumres
        for i in range(length, n):
            sumres += cardPoints[i] - cardPoints[i - length]
            minnum = min(minnum, sumres)
            total += cardPoints[i]
        return total - minnum


cardPoints = [96, 90, 41, 82, 39, 74, 64, 50, 30]
k = 8
print(Solution().maxScore(cardPoints, k))
