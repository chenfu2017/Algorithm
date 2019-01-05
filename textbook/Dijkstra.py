# 最短路径
INF = float('INF')
G = [
    [INF, 10, INF, 5, INF],
    [INF, INF, 1, 2, INF],
    [INF, INF, INF, INF, 4],
    [INF, 3, 9, INF, 2],
    [7, INF, 6, INF, INF],
]
m = len(G)
P = [0] * m
D = [0] * m
S = [False] * m


def ShortestPath_DIJ(vo):
    for v in range(m):
        D[v] = G[vo][v]
        P[v] = vo
    S[vo] = True
    D[vo] = 0
    for i in range(1, m):
        min = INF
        for w in range(m):
            if (not S[w]) and D[w] < min:
                v = w
                min = D[w]
        S[v] = True
        for w in range(m):
            if (not S[w]) and D[v] + G[v][w] < D[w]:
                D[w] = D[v] + G[v][w]
                P[w] = v


def Display(start, temp):
    stack = []
    stack.append(temp)
    while not temp == start:
        stack.append(P[temp])
        temp = P[temp]
    while len(stack):
        if len(stack) > 1:
            print('%s->' % stack.pop(), end='')
        else:
            print(stack.pop())


start = 0
end = 2
ShortestPath_DIJ(start)
print(D)
Display(start, end)
