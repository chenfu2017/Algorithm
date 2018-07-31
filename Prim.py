#最小生成树
INF = 65535
a, b, c, d, e, f = range(6)
G = [
    {b: 10, c: 6},  # a
    {a: 10, d: 2, c: 3, e: 1},  # b
    {a: 6, b: 3, e: 8},  # c
    {b: 2},  # d
    {b: 1, c: 8, f: 7},  # e
    {e: 7}  # f
]
dist = []
P = []
nvisit = [a, b, c, d, e, f]


def init(start):
    for i in range(len(G)):
        if i == start:
            dist.append(0)
        else:
            dist.append(INF)
        P.append(-1)


def getMinIndex(list):
    temp = []
    for i in nvisit:
        temp.append(list[i])
    return list.index(min(temp))


def prim(start):
    init(start)
    visitCount = len(G)
    ans = 0
    while visitCount:
        u = getMinIndex(dist)
        if u !=start:
            P[u] = parent
        ans = ans + dist[u]
        nvisit.remove(u)
        parent = u
        for v in G[u]:
            dist[v] = min(dist[v], G[u][v])
        visitCount -= 1
    return ans


def Display(start):
    print('%s-->' % start, end='')
    for i in range(len(P)):
        if P[i] ==start:
            Display(i)

start = a
print('最小生成树的长度为%s'%prim(start))
Display(start)
print('None')

