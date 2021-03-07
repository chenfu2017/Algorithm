class Solution:
    def __init__(self):
        self.flag = False

    def checkPowersOfThree(self, n: int) -> bool:
        def dfs(i, c):
            if i > 15:
                return
            if c == n:
                self.flag = True
                return
            if self.flag == False:
                dfs(i + 1, c + 3 ** i)
            if self.flag == False:
                dfs(i + 1, c)

        dfs(0, 0)
        return self.flag


n = 91
print(Solution().checkPowersOfThree(n))
