from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = set(wordDict)
        n = len(s)
        dp = [False] *(n+1)
        dp[0] = True
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in m:
                    dp[i] = True
                    break
        return dp[n]


s = "a"
wordDict = ["a"]
print(Solution().wordBreak(s,wordDict))