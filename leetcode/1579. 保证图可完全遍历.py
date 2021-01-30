class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        ufa = UnionFind(n)
        ufb = UnionFind(n)
        ans = 0
        for edge in edges:
            edge[1] -= 1
            edge[2] -= 1

        for t, u, v in edges:
            if t == 3:
                if ufa.union(u, v):
                    ans += 1
                else:
                    ufb.union(u, v)

        for t, u, v in edges:
            if t == 1:
                if ufa.union(u, v):
                    ans += 1
            elif t == 2:
                if ufb.union(u, v):
                    ans += 1

        # print(ufa.getCount())
        # print(ufb.getCount())
        if ufa.getCount()!=1 or ufb.getCount()!=1:
            return -1
        return ans


class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = []
        for i in range(n):
            self.parent.append(i)

    def connected(self, x, y):
        x, y = self.find(x), self.find(y)
        return x == y

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:
            self.parent[rootx] = rooty
            self.count -= 1
            return False
        return True

    def getCount(self):
        return self.count


n = 4
edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
print(Solution().maxNumEdgesToRemove(n, edges))
