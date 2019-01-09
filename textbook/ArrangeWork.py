class Solution:
    def __init__(self):
        self.best = float('INF')
        self.x = []

    def arrange(self, need,i,c,cx):
        n = len(need)
        if i == n:
            if self.best>c:
                self.best=c
                self.x = cx.copy()
            return
        for j in range(n):
            if j not in cx and c+need[i][j]<self.best:
                self.arrange(need,i+1,c+need[i][j],cx+[j])

need=[
    [2,3,3],
    [1,4,3],
    [3,1,2]
]
s = Solution()
s.arrange(need,0,0,[])
print(s.x)
print(s.best)
