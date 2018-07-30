# 拓扑排序
G = {
    'a': set('bc'),
    'b': set('df'),
    'c': set('bd'),
    'd': set('g'),
    'f': set('g'),
    'g': set()
}
deg = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'f': 0,
    'g': 0
}
stack = []
list = []


def initDegree():
    for u, v in G.items():
        for a in G.get(u):
            deg[a] += 1


def topologicalSort():
    initDegree()
    for a in deg:
        if deg[a] == 0:
            stack.append(a)
    count = 0
    while count < len(G) and len(stack):
        u = stack.pop()
        list.append(u)
        for a in G.get(u):
            deg[a] -= 1
            if deg[a] == 0:
                stack.append(a)
        count += 1
    if count < len(G):
        print("有环")
    else:
        print(list)


topologicalSort()
