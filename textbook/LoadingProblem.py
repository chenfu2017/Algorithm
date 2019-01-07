import queue


class Solution:
    """
           node [ub, level, w, x[n]]
           ub 上界 level 搜索空间层级 w 总重量 v 总价值 x[] 解向量
    """

    def __init__(self):
        self.w = [3,2,1]
        self.c1 = 3
        self.c2 = 4
        self.r = sum(self.w)
        self.sum = sum(self.w)
        self.x = [0] * len(self.w)
        self.bestWeight = 0

    def recursion(self):
        def recursion_detail(i, c):
            if i < 0 or c <= 0:
                return 0
            res = recursion_detail(i - 1, c)
            if c >= self.w[i]:
                res = max(res, recursion_detail(i - 1, c - self.w[i]) + self.w[i])
            return res

        cw = recursion_detail(len(s.w) - 1, s.c1)
        r = self.sum - cw
        if r > self.c2:
            print("无法装载!")
        else:
            print("第一艘船装载%d,第二艘船装载%d" % (cw, r))

    def dp(self):
        n = len(self.w)
        m = [[0] * (self.c1 + 1) for _ in range(n)]
        for j in range(self.c1 + 1):
            m[0][j] = [0, self.w[0]][j >= self.w[0]]
        for i in range(1, n):
            for j in range(1, self.c1 + 1):
                if self.w[i] > j:
                    m[i][j] = m[i - 1][j]
                else:
                    m[i][j] = max(m[i - 1][j], m[i - 1][j - self.w[i]] + self.w[i])
        r = self.sum - m[-1][-1]
        if r > self.c2:
            print("无法装载!")
        else:
            j = self.c1
            for i in range(n - 1, -1, -1):
                if m[i][j] > m[i - 1][j] or not i and j:
                    self.x[i] = 1
                    j = j - self.w[i]
            self.bestWeight = m[-1][-1]

    def dfs(self, i, cw, cx):
        if i >= len(self.w):
            if self.bestWeight < cw:
                self.bestWeight = cw
                self.x = cx.copy()
            return
        self.r -= self.w[i]
        if cw + self.w[i] <= self.c1:
            cx[i] = 1
            self.dfs(i + 1, cw + self.w[i], cx)
        if cw + self.r > self.bestWeight:
            cx[i] = 0
            self.dfs(i + 1, cw, cx)
        self.r += self.w[i]

    def push(self, q, node):
        ub, level, w, x = range(4)
        if node[level] == len(self.w):
            print(node)
            if node[w] > self.bestWeight:
                self.bestWeight = node[w]
                self.x = node[x]
        else:
            node[0] = -node[0]
            q.put(node)

    def pop(self, q):
        node = q.get()
        node[0] = -node[0]
        return node

    def bfs(self):
        ub, level, w, x = range(4)
        n = len(self.w)
        q = queue.PriorityQueue()
        node = [self.r,0,0,[0]*n]
        self.push(q,node)
        while not q.empty():
            parent =self.pop(q)
            child_level=parent[level]+1
            i = parent[level]
            cw = parent[w]
            if parent[w] + self.w[i] <= self.c1:
                left = [cw +sum(self.w[i:]), child_level, parent[w] + self.w[i], parent[x].copy()]
                left[x][parent[level]] = 1
                self.push(q, left)
            right = [cw + sum(self.w[i+1:]), child_level, parent[w], parent[x].copy()]
            right[x][i] = 0
            if cw + sum(self.w[i:]) > self.bestWeight:
                self.push(q, right)


s = Solution()
# s.recursion()
# s.dp()
# s.dfs(0, 0, len(s.w) * [0])
s.bfs()
print(s.x)
print(s.bestWeight)
