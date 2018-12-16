# 最小生成树
a, b, c, d, e, f = range(6)
G = [
    {b: 10, c: 6},  # a
    {a: 10, d: 2, c: 3, e: 1},  # b
    {a: 6, b: 3, e: 8},  # c
    {b: 2},  # d
    {b: 1, c: 8, f: 7},  # e
    {e: 7}  # f
]
u = []
v = []
w = []

def quickSort(arr, u, v, low, high):
    if low > high:
        return
    i = low
    j = high
    key = arr[low]
    while i < j:
        while i < j and key <= arr[j]:
            j -= 1
        while i < j and key >= arr[i]:
            i += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[low] = arr[low], arr[i]
    u[i], u[low] = u[low], u[i]
    v[i], v[low] = v[low], v[i]
    quickSort(arr, u, v, low, i - 1)
    quickSort(arr, u, v, i + 1, high)

def init():
    for i in range(len(G)):
        for j in G[i]:
            if i < j:
                u.append(i)
                v.append(j)
                w.append(G[i][j])
    quickSort(w, u, v, 0, len(w) - 1)

def kruskal():
    init()
    ans = 0
    vexset = []
    for i in range(len(G)):
        vexset.append(i)
    for i in range(len(w)):
        v1 = u[i]
        v2 = v[i]
        vs1 = vexset[v1]
        vs2 = vexset[v2]
        if vs1 != vs2:
            print('边%s-->%s的权值%s'%(v1,v2,w[i]))
            ans = ans + w[i]
            for j in range(len(vexset)):
                if vexset[j] == vs2:
                    vexset[j] = vs1
    return ans

print('最小生成树的长度为%s'%kruskal())
