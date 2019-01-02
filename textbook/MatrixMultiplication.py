def fun(p):
    n = len(p)-1
    m = [[float('inf')] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    for i in range(n):
        m[i][i]= 0
    for r in range(2,n+1):
        for i in range(n-r+1):
            j = i+r-1
            for k in range(i,j):
                tmp = m[i][k]+m[k+1][j]+p[i]*p[k+1]*p[j+1]
                if tmp < m[i][j]:
                    m[i][j] = tmp
                    s[i][j] = k
    show(m)
    show(s)
def show(arr):
    for i in arr:
        for j in i:
            print('%8.0f'%j,end='')
        print()


p = [30,35,15,5,10,20,25]
fun(p)
