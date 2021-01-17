def fun(p):
    n = len(p) - 1
    m = [[float('inf')] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    for i in range(n):
        m[i][i] = 0
    for r in range(1, n):
        for i in range(n - r):
            j = i + r
            for k in range(i, j):
                tmp = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                print('m[%d,%d]=m[%d,%d]+m[%d,%d]+p[%d,%d,%d]'%(i,j,i,k,k+1,j,i,k+1,j+1))
                if tmp < m[i][j]:
                    m[i][j] = tmp
                    s[i][j] = k
    show(m)
    show(s)


def show(arr):
    for i in arr:
        for j in i:
            print('%8.0f' % j, end='')
        print()


p = [2,2,1,3,2]
fun(p)
