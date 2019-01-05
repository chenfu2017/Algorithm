d = 4
price = [
    [1, 2, 3],
    [3, 2, 1],
    [3, 2, 2],
]
weight = [
    [1, 2, 3],
    [3, 2, 1],
    [2, 2, 2],
]
min_weight = float('inf')
r = []


def dfs(p, w, i, l):
    global min_weight,c1,c2
    global r
    if i == len(price):
        if w < min_weight:
            min_weight = w
            r = l.copy()
        return
    for j in range(len(price[i])):
        if p + price[i][j] <= d:
            dfs(p + price[i][j], w + weight[i][j], i + 1, l + [j])


dfs(0, 0, 0, [])
print("最小总重量为%d,供应商序号为:%s" % (min_weight, r))

