INF = 65535
G=[
    [INF, 10, 35,200],
    [INF, INF,15 ,40],
    [INF, INF, INF,10],
    [INF, INF, INF,INF],
]

def make_mat(m, n, fill=None):
    mat = []
    for i in range(m):
        mat.append([fill] * n)
    return mat
def init(m):
    for i in range(m):
        for j in range(m):
            D[i][j]=G[i][j]
            P[i][j]=j
def path(i, j):
    k = P[i][j]
    print('%s->'%i,end='')
    while k != j:
        print('%s->'%k,end='')
        k=P[k][j]
    print('%s->' % j, end='')
m = len(G)
P=make_mat(m,m,0)
D=make_mat(m,m,0)
init(m)
for k in range(m):
    for i in range(m):
        for j in range(m):
            if D[i][j] > D[i][k]+D[k][j]:
                D[i][j] = D[i][k] + D[k][j]
                P[i][j] = P[i][k]

print(P)
print(path(0,3))