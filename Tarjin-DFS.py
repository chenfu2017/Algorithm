G = {
    'a': set('bce'),
    'b': set('acd'),
    'c': set('ab'),
    'd': set('b'),
    'e': set('afg'),
    'f': set('eg'),
    'g': set('ef')
}
R = {
    'a': set(''),
    'b': set(''),
    'c': set(''),
    'd': set(''),
    'e': set(''),
    'f': set(''),
    'g': set('')
}
visited = []
low = [0] * len(G)
dfn = [0] * len(G)
for i in range(len(G)):
    visited.append(False)

def getIndex(a):
    return list(G.keys()).index(a)

def exist(u, v):
    for a in R.get(u):
        if a == v:
            return True
    return False

def getParent(u):
    for k in R:
        if exist(k,u):
            return k
    return None

time = 0
def tarjin(u):
    uindex = getIndex(u)
    visited[uindex] = True
    global time
    time = time + 1
    low[uindex] = dfn[uindex] = time
    count = 0
    for v in G.get(u):
        if exist(v, u):
            continue
        vindex = getIndex(v)
        if visited[vindex]:
            low[uindex] = min(low[uindex], dfn[vindex])
        else:
            R.get(u).add(v)
            tarjin(v)
            low[uindex] = min(low[vindex], low[uindex])
            if low[vindex] >= dfn[uindex]:
                count += 1
    if count > 0:
        if dfn[uindex]==1:
            if count > 1:
                print('%s是割点'%u)
        else:
            print('%s是割点'%u)
    if low[uindex] == dfn[uindex] and dfn[uindex]!=1:
        print('%s和%s之间的边为割边'%(u,getParent(u)))
tarjin('a')





