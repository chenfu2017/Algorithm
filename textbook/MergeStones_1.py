class Solution:
    def __init__(self):
        self.sum=[]

    def getSum(self,i,j):
        return self.sum[j]-[self.sum[i-1],0][i<=0]

    def merge(self,stones):
        n = len(stones)
        self.sum.append(stones[0])
        for i in range(1, n):
            self.sum.append(stones[i] + self.sum[i - 1])
        m = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            m[i][i]=0
        for r in range(1,n):
            for i in range(n-r):
                j = i+r
                for k in range(i,j):
                    m[i][j] = min(m[i][j],m[i][k]+m[k+1][j]+self.getSum(i,j))
        return m[0][-1]


s = Solution()
stones=[4,4,5,9]
print(s.merge(stones))
