class Solution:

    def hire(self,moneys):
        n = len(moneys)
        m = [[0]*(n+1) for _ in range(n+1)]
        for i in range(0,n):
            len_m = len(moneys[i])
            for j in range(0,len_m):
                m[i][j+n-len_m+1]=moneys[i][j]
        for r in range(1,n):
            for i in range(n-r):
                j = i+r+1
                for k in range(i,j):
                    m[i][j]=min(m[i][j],m[i][k]+m[k][j])
        print(m)
        return m[0][-1]


moneys=[
    [5,15,19],
    [7,11],
    [3]
]
print(Solution().hire(moneys))