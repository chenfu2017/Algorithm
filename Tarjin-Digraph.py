#求有向图强连通分量
G = {
    'a': set('bc'),
    'b': set('gc'),
    'c': set(''),
    'd': set('b'),
    'e': set('f'),
    'f': set('g'),
    'g': set('e')
}

visited = []
stack = []
low = [0] * len(G)
dfn = [0] * len(G)
for i in range(len(G)):
    visited.append(False)

def getIndex(a):
    return list(G.keys()).index(a)

time = 0
def tarjin(u):
    uindex = getIndex(u)
    visited[uindex] = True
    global time
    time = time + 1
    stack.append(u)
    low[uindex] = dfn[uindex] = time
    for v in G.get(u):
        vindex = getIndex(v)
        if visited[vindex]:
            if v in stack:
                low[uindex] = min(low[uindex], dfn[vindex])
        else:
            tarjin(v)
            low[uindex] = min(low[vindex], low[uindex])
    if low[uindex] == dfn[uindex]:
        print("强连通分量的集合:{",end='')
        w = stack.pop()
        while w !=u:
            print(w,end=',')
            w =stack.pop()
        print(u,end='}\n')
tarjin('a')





