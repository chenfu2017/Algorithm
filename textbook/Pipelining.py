class Solution:
    def __init__(self):
        self.bestf = float('inf')
        self.bestx = []

    def dowork(self,f,s,i,f1,f2,x):
        n = len(f)
        if i == n:
            if f2[i-1]<self.bestf:
                self.bestf = f2[i-1]
                self.bestx=x.copy()
            print(f2)
            return
        for j in range(i, n):
            f1 +=f[x[j]]
            f2[i]= max(f[x[j]], f2[i - 1]) + s[x[i]]
            # if f2[i]<self.bestf:
            x[i], x[j]= x[j], x[i]
            self.dowork(f,s,i + 1, f1+f[x[j]],max(f1, f2[i - 1]) + s[x[i]],x)
            x[i], x[j]= x[j], x[i]
            f1-=f[x[j]]


f=[2,2,3]
s=[3,1,1]
n = len(f)
f2 =[0]*n
x =[i for i in range(n)]
solution = Solution()
solution.dowork(f,s,0,0,f2,x)



