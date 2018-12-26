d = 4
price = [
    [1, 2, 3],
    [3, 2, 1],
    [2, 3, 2],
]
weight = [
    [1, 2, 3],
    [3, 2, 1],
    [2, 2, 2],
]
min_price= float('inf')
r = []
def dfs(p, w, index, l):
    global min_price
    global r
    if p > d:
        return
    if index == len(price):
        if p < min_price:
            min_price = p
            r = l.copy()
        return
    for i in range(len(price[0])):
        l.append(i)
        dfs(p + price[index][i], w + weight[index][i], index + 1, l)
        l.pop()
l = []
dfs(0, 0, 0, l)
print("最小总价值为%d,供应商序号为:%s"%(min_price,r))

