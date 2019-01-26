class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(i, c, l):
            if c == target:
                res.append(list(l))
                return
            for j in range(i, len(candidates)):
                if c + candidates[j] > target:
                    return
                dfs(j, c + candidates[j], l + [candidates[j]])

        candidates.sort()
        dfs(0, 0, [])
        return res


candidates = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(candidates, target))
