# 最短路径
INF = 65535
G = [
    [INF, 10, 35, 200],
    [INF, INF, 15, 40],
    [INF, INF, INF, 10],
    [INF, INF, INF, INF],
]
D = []


def getEdges(G):
    v = []  # 出发点
    u = []  # 对应的相邻到达点
    w = []  # 顶点v1到顶点v2的边的权值
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != INF:
                w.append(G[i][j])
                v.append(i)
                u.append(j)
    print(v)
    print(u)
    print(w)
    return v, u, w


def initDist(vo):
    for k in range(len(G)):
        if k == vo:
            D.append(0)
        else:
            D.append(INF)


def ShortestPath_BF(vo):
    initDist(vo)
    v, u, w = getEdges(G)
    flag = True
    count = 0
    for k in range(len(G) - 1):  # 循环 n-1轮
        flag = False
        for i in range(len(w)):  # 对每条边进行一次松弛操作
            if D[u[i]] > w[i] + D[v[i]]:
                D[u[i]] = D[v[i]] + w[i]
                flag = True
        count = count + 1
        if flag == False: break
    if count == len(G) - 1:
        print('有负环')


start = 0
ShortestPath_BF(start)
print(D)
