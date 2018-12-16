tone = [4, 4, 5, 9]
n = len(tone)
sum=[]
for i in range(n):
    if i==0:
        sum.append(tone[0])
    else:
        sum.append(sum[i - 1] + tone[i])
def getSum(i, j):
    if i + j >= n:
        return getSum(i, n - i - 1) + getSum(0, i + j - n)
    else:
        if i > 0:
            return sum[i + j] - sum[i - 1]
        else:
            return sum[i + j]


def find():
    dp_min = [[float('inf')] * n for _ in range(n)]
    dp_max = [[0] * n for _ in range(n)]
    for i in range(n):
        dp_min[i][0] = 0
    for j in range(1, n):
        for i in range(n):
            dp_min[i][j] = float('inf')
            for k in range(j):
                dp_max[i][j] = max(dp_max[i][j], dp_min[i][k] + dp_max[(i + k + 1) % n][j - k - 1] + getSum(i, j))
                dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[(i + k + 1) % n][j - k - 1] + getSum(i, j))
    print(dp_min)
    print(dp_min[0][n - 1])
    print(dp_min)
    print(dp_max[0][n - 1])
find()
