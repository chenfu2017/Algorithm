class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        res = 0
        n = len(strs)
        uf = UnionFind(n)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if not uf.connect(i, j) and self.check(strs[i], strs[j]):
                    uf.union(i, j)
        for i in range(n):
            if uf.parent[i] == i:
                res += 1
        return res

    def check(self, m, n):
        num = 0
        for i, j in zip(m, n):
            if i != j:
                num += 1
            if num > 2:
                return False
        return True


class UnionFind:
    def __init__(self, n):
        self.parent = []
        for i in range(n):
            self.parent.append(i)

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x

    def connect(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        return rootx == rooty

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:
            self.parent[rootx] = rooty


strs = ["tars", "rats", "arts", "star"]
print(Solution().numSimilarGroups(strs))
