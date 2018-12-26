class Solution:
    def generateParenthesis(self, n):
        ans = []

        def dfs(S='', left=0, right=0):
            if left > n or right > left:
                return
            if len(S) == 2 * n:
                ans.append(S)
                return
            dfs(S + '(', left + 1, right)
            dfs(S + ')', left, right + 1)

        dfs()
        return ans


print(Solution().generateParenthesis(4))
