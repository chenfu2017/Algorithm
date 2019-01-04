import queue


class Solution:
    """
           node [ub, level, w, v, x[n]]
           ub 上界 level 搜索空间层级 w 总重量 v 总价值 x[] 解向量
    """

    def __init__(self):
        self.v = [6, 10, 12]
        self.w = [1, 2, 3]
        self.x = [0] * len(self.v)
        self.bestValue = 0

    def recursion(self, i, c):
        if i < 0 or c <= 0:
            return 0
        r1 = self.recursion(i - 1, c)
        if c >= self.w[i]:
            r2 = self.recursion(i - 1, c - self.w[i]) + self.v[i]
            return max(r1,r2)


def dp(self, capacity):
    n = len(self.w)
    m = [[0] * (capacity + 1) for _ in range(n)]
    for j in range(capacity + 1):
        m[0][j] = [0, self.v[0]][j >= self.w[0]]
    for i in range(1, n):
        for j in range(1, capacity + 1):
            if self.w[i] > j:
                m[i][j] = m[i - 1][j]
            else:
                m[i][j] = max(m[i - 1][j], m[i - 1][j - self.w[i]] + self.v[i])
    j = capacity
    for i in range(n - 1, -1, -1):
        if m[i][j] > m[i - 1][j] or not i and j:
            self.x[i] = 1
            j = j - self.w[i]
    self.bestValue = m[-1][-1]
    return m[-1][-1]


def backtracking(self, capacity, i, cv, cw, cx):
    if i >= len(self.w):
        if self.bestValue < cv:
            self.bestValue = cv
            self.x = cx.copy()
        return
    if cw + self.w[i] <= capacity:
        cx[i] = 1
        self.backtracking(capacity, i + 1, cv + self.v[i], cw + self.w[i], cx)
    cx[i] = 0
    node = [0, i + 1, cw, cv, None]
    self.bound(capacity, node)
    if node[0] > self.bestValue:
        self.backtracking(capacity, i + 1, cv, cw, cx)


def bound(self, capacity, node):
    n = len(self.v)
    i, sumw, sumv = node[1], node[2], node[3]
    while i < n and sumw + self.w[i] <= capacity:
        sumw += self.w[i]
        sumv += self.v[i]
        i += 1
    if i < n:
        node[0] = sumv + (capacity - sumw) * self.v[i] / self.w[i]
    else:
        node[0] = sumv


def push(self, q, node):
    ub, level, w, v, x = range(5)
    if node[level] == len(self.v):
        if node[v] > self.bestValue:
            self.bestValue = node[v]
            self.x = node[x]
    else:
        node[0] = -node[0]
        q.put(node)


def pop(self, q):
    node = q.get()
    node[0] = -node[0]
    return node


def branchBounding(self, capacity):
    ub, level, w, v, x = range(5)
    n = len(self.v)
    q = queue.PriorityQueue()
    node = [0, 0, 0, 0, [0] * n]
    self.bound(capacity, node)
    self.push(q, node)
    while not q.empty():
        parent = self.pop(q)
        child_level = parent[level] + 1
        i = parent[level]
        if parent[w] + self.w[parent[level]] <= capacity:
            left = [0, child_level, parent[w] + self.w[i], parent[v] + self.v[i], parent[x].copy()]
            left[x][parent[level]] = 1
            self.bound(capacity, left)
            self.push(q, left)
        right = [0, child_level, parent[w], parent[v], parent[x].copy()]
        right[x][i] = 0
        self.bound(capacity, right)
        if right[ub] > self.bestValue:
            self.push(q, right)


solution = Solution()
# solution.dp(5)
# solution.backtracking(5, 0, 0, 0, [0] * 3)
# solution.branchBounding(5)
solution.bestValue=solution.recursion(len(solution.v) - 1, 5)
print(solution.bestValue)
# print(solution.x)

