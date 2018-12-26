class Solution:
    def generateParenthesis(self, n):
        ans = []
        def dfs(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                dfs(S+'(', left+1, right)
            if right < left:
                dfs(S+')', left, right+1)

        dfs()
        return ans

print(Solution().generateParenthesis(3))