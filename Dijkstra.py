#最短路径
INF = 65535
G = [
    [INF, 10, 35, 200],
    [INF, INF, 15, 40],
    [INF, INF, INF, 10],
    [INF, INF, INF, INF],
]
P = []
D = []
S = []
def init(m):
    for i in range(m):
        P.append(0)
        D.append(0)
        S.append(False)

m = len(G)
init(m)
def ShortestPath_DIJ(vo):
    for v in range(m):
        S[v] = False
        D[v] = G[vo][v]
        if [D[v] < INF]:
            P[v] = vo
        else:
            P[v] = -1
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
        if len (stack)>1 :
            print('%s->'%stack.pop(),end='')
        else:
            print(stack.pop())

start = 0
end = 3
ShortestPath_DIJ(start)
print(P)
print(D)
Display(start,end)
