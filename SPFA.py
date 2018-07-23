INF = 65535
G = [
    [INF, 10, 35, 200],
    [INF, INF, 15, 40],
    [INF, INF, INF, 10],
    [INF, INF, INF, INF],
]
D = []
def getEdges(G):
    u = []  # 出发点
    v = []  # 对应的相邻到达点
    w = []  # 顶点v1到顶点v2的边的权值
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != INF:
                w.append(G[i][j])
                u.append(i)
                v.append(j)
    print(u)
    print(v)
    print(w)
    return u, v, w
def initDist(vo):
    for k in range(len(G)):
        if k == vo:
            D.append(0)
        else:
            D.append(INF)

def ShortestPath_SPFA(vo):
    initDist(vo)
    u, v, w = getEdges(G)
    q = []
    q.append(vo)
    count = 0
    while len(q) and count < len(G)*len(u):
        top = q.pop(0)
        for i in range(len(u)):  # 对每条边进行一次松弛操作
            if top == u[i] and D[u[i]] + w[i] < D[v[i]] :
                D[v[i]] = D[u[i]] + w[i]
                if v[i] not in q:
                    q.append(v[i])
        count = count + 1
start = 2
ShortestPath_SPFA(start)
print(D)


